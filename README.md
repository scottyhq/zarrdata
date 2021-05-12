# zarrdata
A convenient way to store a publically-accessible [Zarr](https://zarr.readthedocs.io/en/stable/) dataset that is versioned and optionally tied to a [Zenodo DOI](https://guides.github.com/activities/citable-code/). 

The basic idea is to host a small amount of data on a static GitHub pages website so that your tutorial, research code, benchmarking suite, etc. can run against a citeable dataset.

*A key limitation of this approach is that Zarr chunks must be less than 100MB*, per [GitHub repository limits](https://docs.github.com/en/github/managing-large-files/what-is-my-disk-quota#file-and-repository-size-limitations). The goal here is a smallish citeable record (<10GB), if you're dealing with really large data or want high-performance you probably want to store the data on AWS S3, GCS, etc...

## Configuration steps

1. Add zarr data
In the [create_zarr.py](./create_zarr.py) script I just create a Zarr store from the Xarray tutorial dataset, but if you have data.zarr you just add it to your repo

1. Add a jekyll configuration file
GitHub pages automatically deploys your repository and serves static HTTP via Jekyll. Because Jekyll ignores hidden files (.zattrs, .zmetadata, etc) by defauly you need a [_config.yml](./_config_yml) to ensure those files are added

1. Enable github pages
To publish the site you just need to enable [GitHub Pages](https://guides.github.com/features/pages/) for the repository. It's as simple as going to repository Settings->Pages->Source (select 'main' branch and 'Save')! The you'll have a live HTTP-website with the repo README.md rendered! For this repo https://github.com/scottyhq/zarrdata the website is https://scottyhq.github.io/zarrdata . 

1. Read your data!
```python
import xarray as xr
import fsspec
uri = 'https://scottyhq.github.io/zarrdata/air_temperature.zarr'
ds = xr.open_dataset(uri, engine="zarr", consolidated=True)
ds.air.isel(time=1).plot(x="lon")
```