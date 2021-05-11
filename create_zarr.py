#!/usr/bin/env python
'''
create an example zarr dataset
'''
import xarray as xr

ds = xr.tutorial.load_dataset("air_temperature", engine="netcdf4")
ds.air.isel(time=1).plot(x="lon")

ds.to_zarr("air_temperature.zarr", consolidated=True)

dsz = xr.open_dataset("air_temperature.zarr", engine="zarr")
dsz.air.isel(time=1).plot(x="lon")
