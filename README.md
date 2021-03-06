# zarrdata
[![DOI](https://zenodo.org/badge/366521090.svg)](https://zenodo.org/badge/latestdoi/366521090)

A convenient way to store a publically-accessible [Zarr](https://zarr.readthedocs.io/en/stable/) dataset that is versioned and optionally tied to a [Zenodo DOI](https://guides.github.com/activities/citable-code/):

```python
import xarray as xr
import fsspec
uri = 'https://scottyhq.github.io/zarrdata/air_temperature.zarr'
ds = xr.open_dataset(uri, engine="zarr", consolidated=True)
ds.air.isel(time=1).plot(x="lon")
```

![Unknown](https://user-images.githubusercontent.com/3924836/117900937-a0e15200-b30d-11eb-9802-f542cc57efcc.png)

The basic idea is to host a smallish citeable record (<1GB) on a static GitHub pages website so that your tutorial, research code, benchmarking suite, etc. can run against a citeable dataset.

*Key limitation of this approach is that Zarr chunks must be less than 100MB, per [GitHub repository limits](https://docs.github.com/en/github/managing-large-files/what-is-my-disk-quota#file-and-repository-size-limitations) and the total size of the repo/zarr store should be less than 1GB per [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#usage-limits)*. If you're dealing with data>1GB or want high-performance you probably want to store the data files on AWS S3, GCS, etc...

## Configuration steps

1. Add zarr data
In the [create_zarr.py](https://github.com/scottyhq/zarrdata/blob/main/create_zarr.py) script I just create a Zarr store from the Xarray tutorial dataset, but if you have data.zarr you just add it to your repo

1. Add a jekyll configuration file
GitHub pages automatically deploys your repository and serves static HTTP via Jekyll. Because Jekyll ignores hidden files (.zattrs, .zmetadata, etc) by default you need a [_config.yml](https://github.com/scottyhq/zarrdata/blob/main/_config.yml) to ensure those files are added

1. Enable github pages
To publish the site you just need to enable [GitHub Pages](https://guides.github.com/features/pages/) for the repository. It's as simple as going to repository Settings->Pages->Source (select 'main' branch and 'Save')! The you'll have a live HTTP-website with the repo README.md rendered! For this repo https://github.com/scottyhq/zarrdata the website is https://scottyhq.github.io/zarrdata . 
