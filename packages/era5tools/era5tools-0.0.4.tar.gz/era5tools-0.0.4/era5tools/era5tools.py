#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import datetime as dt
import pandas as pd
import xarray as xr
import cdsapi
import climperiods


class ERA5():
    def __init__(self, cdsapi_key, varmap={}, varmap_da={}):
        """Convenience class for downloading and processing ECMWF
        ERA5 reanalysis.

        Parameters
        ----------
        cdsapi_key : str
            Copernicus CDSAPI key.
        varmap : dict
            Mapping from short to long ERA5 variable names.
            Default variables include pre, tmp and sst.
        varmap_da : dict
            Mapping from short to ERA5 variable names in the downloaded files.
            Default variables include pre, tmp and sst.
        """

        # List available precomputed climatologies for calculating anomalies
        self.climpath = os.path.join(os.path.dirname(__file__), 'clims')
        self.clims_available = sorted([f.split('.')[0]
                                       for f in os.listdir(self.climpath)
                                       if 'zarr' in f and not f.startswith('.')])
        self.clim = None

        # Need a Copernicus Data Store Beta (CDS-Beta) API key
        self.c = cdsapi.Client(key=cdsapi_key,
                               url='https://cds-beta.climate.copernicus.eu/api')

        # Mapping from short to long ERA5 variable names
        self.varmap = {'pre': 'total_precipitation',
                       'tmp': '2m_temperature',
                       'sst': 'sea_surface_temperature',
                       **varmap}

        # Mapping from short to ERA5 variable names in the DataArray
        self.varmap_da = {'pre': 'tp',
                          'tmp': 't2m',
                          'sst': 'sst',
                          **varmap_da}

    def _get_era5_monthly_means(self, outpath, vname, year, month=None):
        """Retrieve ERA5 reanalyis *monthly means* in grib format.
        """

        if month is None:
            fname = f'{vname}_{year}.grib'
            months = [str(m) for m in range(1, 13)]
        else:
            fname = f'{vname}_{year}_{month:02}.grib'

        self.c.retrieve('reanalysis-era5-single-levels-monthly-means',
                        {'product_type': 'monthly_averaged_reanalysis',
                         'format': 'grib',
                         'variable': self.varmap[vname],
                         'year': str(year),
                         'month': months if month is None else f'{month:02}',
                         'time': '00:00'}
                       ).download(os.path.join(outpath, fname))

    def download(self, vname, outpath, data_type='slmm', year_range=(None,None),
                 months=None, overwrite=False, skip_error=False):
        """Download ERA5 data on single levels for a single variable.

        Parameters
        ----------
            vname : str
                Variable name (internal).
            outpath : str
                Output path to save files.
            data_type : str, optional
                Type of data to download. Ignored for now as only current
                option is 'slmm' - single level monthly means.
            year_range : (int, int), optional
                Year range to download.
            months : list, optional
                List of months to download. Defaults to full year.
            overwrite : boolean, optional
                If True, don't check for existence of file before downloading.
                Defaults to False.
            skip_error : boolean, optional
                If True, skips any download errors via try-except.
                Defaults to True.
        """

        years = range(year_range[0], year_range[1]+1)
        if months is None:
            months = range(1,13)

            # Loop over years
            for year in years:
                fname = f'{vname}_{year}.grib'
                if not overwrite and os.path.exists(os.path.join(outpath, fname)):
                    print(f'Skipping {fname} as it exists in directory.')
                else:
                    if skip_error:
                        try:
                            self._get_era5_monthly_means(outpath, vname, year)
                        except:
                            print(f'*** FAILED {vname} {year} ***')
                    else:
                        self._get_era5_monthly_means(outpath, vname, year)
        else:
            # Loop over years and months
            for year in years:
                for month in months:
                    fname = f'{vname}_{year}_{month:02}.grib'
                    if not overwrite and os.path.exists(os.path.join(outpath, fname)):
                        print(f'Skipping {fname} as it exists in directory.')
                    else:
                        if skip_error:
                            try:
                                self._get_era5_monthly_means(outpath, vname, year, month)
                            except:
                                print(f'*** FAILED {vname} {year}-{month:02} ***')
                        else:
                            self._get_era5_monthly_means(outpath, vname, year, month)

    def convert(self, ds, vname, lat_range=(None,None), lon_range=(None,None)):
        """Convert units and structure of raw files.

        Currently supported variables:
            pre - precipitation [tp, m => mm]
            tmp - 2m temperature [t2m, K => C]
            sst - sea surface temperature [sst, K => C]

        Parameters
        ----------
            ds : xarray Dataset or DataArray
                Dataset or DataArray with dims
                ['step','latitude','longitude'].
            vname : str
                Variable name (internal).
            lat_range : (float, float), optional
                Latitude range subset to use.
            lon_range : (float, float), optional
                Longitude range subset to use.

        Returns
        -------
            ds : xarray Dataset or DataArray
                Converted Dataset or DataArray.
        """

        secs_per_day = 86400
        mm_per_m = 1000
        K_to_C = -273.15

        # Drop unneeded dims/coords
        ds = ds.drop(['number','step','surface','valid_time'])

        # Convert longitudes from 0->360 to -180->180
        ds['longitude'] = ((ds['longitude'] + 180) % 360) - 180
        ds = ds.sortby(['latitude','longitude'])

        if vname == 'pre':
            # Precipitation conversion factor from m to mm
            ds = ds['tp'] * mm_per_m
        elif vname in ['t2m','sst']:
            # Temperature conversion from Kelvin to Celsius
            ds = ds[self.varmap_da[vname]] + K_to_C
        else:
            print(f'vname must be one of {list(self.varmap_da.keys())}')
            return None

        # Slice to lat/lon bounding box and return
        ds = ds.sel(latitude=slice(*lat_range), longitude=slice(*lon_range))
        return ds

    def _to_monthly(self, ds):
        """Convert timestamp dimension into ['year','month'] dimensions."""
        year = ds.time.dt.year
        month = ds.time.dt.month

        # Assign new coords
        ds = ds.assign_coords(year=('time', year.data), month=('time', month.data))

        # Reshape the array to (..., 'month', 'year')
        return ds.set_index(time=('year', 'month')).unstack('time')

    def proc(self, inpath, vname, year_range=(None, None), to_monthly=True,
             lat_range=(None, None), lon_range=(None, None)):
        """Process multiple ERA5 reanalysis files for a single variable.

        Process reanalysis data on single levels for a single variable.
        Assumes standard ERA5 file structure with an internally-defined
        filename convention, and files in xarray Dataset format with dimensions
        [time, latitude, longitude], converts to a Dataset with the same
        dimensions, or [year, month, latitude, longitude] if to_monthly is True.

        Parameters
        ----------
            inpath : str
                Path to SEAS5 grib files by month and variable.
            vname : str
                Variable name (internal).
            year_range : (int, int), optional
                Year range to process.
            to_monthly : boolean, optional
                Convert datetimes to (year, month) dimensions.
            lat_range : (float, float), optional
                Latitude range subset to use to fit the model.
            lon_range : (float, float), optional
                Longitude range subset to use to fit the model.

        Returns
        -------
            ds : xarray.Dataset
                Processed Dataset.
        """

        # Generate all file paths - assumes either yearly or monthly files
        years = range(year_range[0], year_range[1]+1)
        fnames = [fname for fname in os.listdir(inpath)
                  if vname in fname and 'grib' in fname and 'idx' not in fname]
        # Check if all years requested are available in fnames
        years_fnames = [int(fname.split('_')[1][:4]) for fname in fnames]
        years_missing = set(years) - set(years_fnames)
        if len(years_missing) > 0:
            print(f'Warning: some years in year_range not in {inpath}:\n'
                  f'{", ".join(map(str, years_missing))}')
            return None

        # Filename template {vname}_{year}.grib or {vname}_{year}_{month}.grib
        fpaths = [os.path.join(inpath, fname) for fname in fnames
                  if int(fname.split('_')[1][:4]) in years]

        # Generate combined DataArray for all months for this variable
        ds = xr.concat([self.convert(xr.open_dataset(fpath, engine='cfgrib',
                                                     backend_kwargs={'indexpath':''}),
                                     vname=vname, lat_range=lat_range,
                                     lon_range=lon_range) for fpath in fpaths],
                                     dim='time').sortby('time')
        return ds if not to_monthly else self._to_monthly(ds)

    def calc_clim(self, inpath, vname, year_range):
        """Calculate a single climatology for a year range.

        Takes the average over all grid locations and months over the
        year_range passed. Assumes time dimension converted to [year, month].

        Parameters
        ----------
            inpath : str
                Input path to raw download data.
            vname : str
                Variable name (internal).
            year_range : (int, int)
                Year range to process.

        Returns
        -------
            ds : xarray.Dataset
                Climatology Dataset.
        """
        data = self.proc(inpath, vname, year_range)
        if data is not None:
            return data.mean(dim='year'
                             ).assign_attrs(desc=f'{vname} climatology',
                                            clim_range=year_range)
        else:
            return None

    def calc_clims(self, inpath, vname, year_range):
        """Calculate multiple climatologies for all years in a year range.

        Calculates NOAA 30-year centred climatologies in 5-year chunks and saves
        in self.climpath. Assumes the time dimension converted to [year, month].

        Parameters
        ----------
            inpath : str
                Input path to raw download data.
            vname : str
                Variable name (internal).
            year_range : (int, int)
                Year range to process.
        """
        for year_from, year_to in climperiods.clims(*year_range).drop_duplicates().values:
            clim = self.calc_clim(inpath, vname, (year_from, year_to))
            out_fpath = os.path.join(self.climpath, f'{vname}_{year_from}_{year_to}.zarr')
            if clim is not None and not os.path.exists(out_fpath):
                clim.to_zarr(out_fpath)

    def load_clim(self, vname, year_range):
        """Load precomputed climatology.

        Parameters
        ----------
            vname : str
                Variable name (internal).
            year_range : (int, int)
                Climatology year range to load.
        """

        fname =  f'{vname}_{year_range[0]}_{year_range[1]}.zarr'
        self.clim = xr.open_dataset(os.path.join(self.climpath, fname),
                                    engine='zarr')[vname]
        return self.clim

    def calc_anoms(self, inpath, vname, year_range):
        """Calculate anomalies from reanalysis and climatology.

        Generates climatologies using standard NOAA 30-year rolling
        window which changes every 5 years. Assumes raw data has been
        processed to have year and month dimensions.

        Parameters
        ----------
            inpath : str
                Input path to raw download data.
            vname : str
                Variable name (internal).
            year_range : (int, int)
                Year range of data to process.

        Returns
        -------
            anoms : xarray.Dataset
                Processed anomalies Dataset.
        """

        anoms = []
        # Generate year ranges used to calculate climatology for each year
        clims = climperiods.clims(*year_range)

        # Loop over climatology year ranges
        for year_range_clim, df in clims.groupby(['year_from','year_to']):
            clim = self.load_clim(vname, year_range_clim)
            data = self.proc(inpath, vname, (df.index.min(), df.index.max()))
            anoms.append(data - clim)
        return xr.concat(anoms, dim='year')


# If running the module as a whole, only download a single month's forecast
if __name__ == '__main__':
    # Always assume that cdsapi_key, outpath and vname will be passed
    cdsapi_key = sys.argv[1]
    outpath = sys.argv[2]
    vname = sys.argv[3]

    era5 = ERA5(cdsapi_key)
    if len(sys.argv) == 4:
        # No year or month passed
        now = dt.date.today()
        era5.download(vname, outpath, year_range=(now.year, now.year),
                      months=[now.month], overwrite=False)
    else:
        year = sys.argv[4]
        month = sys.argv[5]
        era5.download(vname, outpath, year_range=(int(year), int(year)),
                      months=[int(month)], overwrite=False)
