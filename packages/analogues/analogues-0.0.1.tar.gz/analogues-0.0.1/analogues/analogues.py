#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import xarray as xr
import quadgrid as qg
from sklearn.decomposition import PCA

class AnalogueSST():
    def __init__(self, res, interp_meth='nearest', lon_range=(-180,180),
                 lat_range=(-90,90), weighting='rootcoslat', metric='euclidean',
                 lon_name='longitude', lat_name='latitude'):
        """Class constructor for Sea Surface Temperature (SST) analogues.

        Parameters
        ----------
            res : float
                Resolution in decimal degrees of the common grid.
            interp_meth : str, optional
                Interpolation method for transforming data to common grid. One
                of the standard methods used by xarray.interp_like(). Defaults
                to 'nearest'.
            lon_range : (float, float), optional
                Longitude range subset to use.
            lat_range : (float, float), optional
                Latitude range subset to use.
            weighting : str, optional
                Weighting to apply to cells before processing. One of 
                  'rootcoslat' - sqrt(cosine(latitude)) [default] or
                  'coslat' - cosine(latitude)
            metric : str, optional
                Similarity metric to use to calculate nearest analogue. One of
                  'euclidean' - Euclidean distance [default] or
                  'cosine' - cosine similarity
            lon_name : str, optional
                Longitude name in the reference and input datasets. Defaults
                to 'longitude' consistent with ERA5 and SEAS5 products.
            lat_name : str, optional
                Latitude name in the reference and input datasets. Defaults
                to 'latitude' consistent with ERA5 and SEAS5 products.
        """

        self.res = res
        self.lon_range = lon_range
        self.lat_range = lat_range
        self.weighting = weighting
        self.metric = metric
        self.interp_meth = interp_meth
        self.lon_name = lon_name
        self.lat_name = lat_name

        # Create common uniform grid for historic/stochastic/forecasts
        self.urg = qg.QuadGrid(res).to_xarray().rename({'lon': lon_name, 'lat': lat_name})

        self.EOFs = {}
        self.PCs = {}
        self.varexp = {}

    def fit(self, da):
        """Calculate EOFs and PCs of reference data.

        Parameters
        ----------
            da : xarray DataArray
                DataArray with dims ['latitude','longitude','year','month'].
        """

        # Interpolate to grid at desired resolution, subset lon/lat and weight
        da_common = da.interp_like(self.urg, method=self.interp_meth
                                  ).sel({self.lon_name: slice(*self.lon_range),
                                         self.lat_name: slice(*self.lat_range)})
        # Calculate weights
        if self.weighting == 'coslat':
            self.weights = np.cos(np.deg2rad(da_common[self.lat_name]))
        elif self.weighting == 'rootcoslat':
            self.weights = np.sqrt(np.cos(np.deg2rad(da_common[self.lat_name])))
        else:
            self.weights = 1

        # Calculate EOFs and PCs for each month
        pca = PCA()
        for m in range(1, 13):
            da_month = da_common.sel(month=m) * self.weights
            X = da_month.to_series().dropna().unstack([self.lat_name, self.lon_name])
            pca.fit(X)
            self.EOFs[m] = pd.DataFrame(pca.components_, columns=X.columns)
            self.PCs[m] = X @ self.EOFs[m].T
            self.varexp[m] = pca.explained_variance_ratio_

    def predict(self, da):
        """Project new data onto fitted EOFs and select analogues.
        
        Can project a single month or multiple versions of the same month
        (e.g. stochastic set or forecast ensembles).

        Parameters
        ----------
            da : xarray DataArray
                DataArray with dims ['latitude','longitude'] with optionally
                'year' [e.g. same month, multiple years] or 
                'number' [multiple ensembles].

        Returns
        -------
            similarity : DataFrame
                Similarity metrics between all reference and input years.
        """

        # Define EOFs and PCs for the month of the current input data
        EOFs = self.EOFs[da['month'].values.max()]
        PCs = self.PCs[da['month'].values.max()]
        varexp = self.varexp[da['month'].values.max()]
        
        # Interpolate to grid at desired resolution, subset lon/lat and weight
        da_common = da.interp_like(self.urg, method=self.interp_meth
                                  ).sel({self.lon_name: slice(*self.lon_range),
                                         self.lat_name: slice(*self.lat_range)}
                                       ) * self.weights
        X = da_common.to_series().dropna().unstack([self.lat_name, self.lon_name])

        # Identify common cells and project data onto EOFs to get predicted PCs
        ix = X.columns.intersection(EOFs.columns)
        PCs_pred = X[ix] @ EOFs[ix].T

        # Calculate similarity to fitted PCs
        if self.metric == 'cosine':
            a = PCs/np.linalg.norm(PCs, axis=1)[:,None]
            b = PCs_pred/np.linalg.norm(PCs_pred, axis=1)[:,None]
            similarity = a @ b.T
        elif self.metric == 'euclidean':
            a = PCs_pred.values[:,None,:]
            b = PCs.values
            similarity = -pd.DataFrame(((a-b)**2 * varexp).sum(axis=2), 
                                       index=PCs_pred.index, columns=PCs.index).T
        else:
            print('similarity metric must be cosine or euclidean')
            similarity = None

        self.similarity = similarity
        self.analogues = similarity.idxmax()
        self.analogue_counts = self.analogues.value_counts()

        return similarity
