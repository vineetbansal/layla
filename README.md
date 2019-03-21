# layla

Boilerplate for a starter Python package meant to go on PyPI or Anaconda Cloud

The source is heavily commented to point out certain concepts.

Basic workflow:

1. `conda update conda` and `conda install conda-build` (in base/default environment - conda-build uses the base environment for everything anyway).

1. Create and activate the `build` environment (we'll need `twine` for pypi uploading)

1. `python setup.py sdist bdist_wheel`

2. Upload pip installable package on Test PyPi

`python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

3. Create and activate a barebones `deploy` environment.

`pip install -i https://test.pypi.org/simple/ layla`

Check to make sure it works. If everything looks good, continue.

4.Upload pip installable package on PyPi

`python -m twine upload dist/*`

## Conda package upload

1. Update meta.yaml with latest version.

1. We're purposely being verbose in the following command so we can see exactly what's going on.

1. `conda-build . --no-anaconda-upload --output-folder conda_dist`

This *should* fail, because importib_resources>=1.0.2 is not available on Anaconda. The reason `conda-build` even cares about this is because it's trying to create and activate a temporary environment where it can install and test your package. Let's fix this:

  1. `conda config --get channels`
     I don't see `conda-forge` listed here, which is good.
     
  1. `conda config --add channels conda-forge`
      `conda config --get channels`
      I now see `conda-forge` in the list, but I've added it as the highest-priority channel. We almost never want to do this, otherwise we're opening ourselves up for a lot of pain. `conda-forge` should be consulted if the regular channel fails.

  1. `conda config --remove channels conda-forge`
  1. `conda config --append channels conda-forge`
      `conda config --get channels`
      Things look better now.
      
1. `conda-build . --no-anaconda-upload --output-folder conda_dist`
   This should build fine now. You'll see a bunch of files in `conda_dist`, `noarch/layla-0.1.3-py_0.tar.bz2` is the one we want.
   
1. `anaconda upload conda_dist/noarch/layla-0.1.3-py_0.tar.bz2`

1. Let's not keep the `conda-forge` channel lingering around our environment.
   `conda config --remove channels conda-forge`
   
1. Create and activate a barebones `deploy` environment. Install our package in it
   `conda install -c vineetbansal layla`
   
  Again, this complains:
  ```
  PackagesNotFoundError: The following packages are not available from current channels:

  - layla -> importlib_resources[version='>=1.0.2']
  ```
   
  As package authors, we shouldn't assume the responsibility of installing dependencies from non-standard (yes, even `conda-forge`) locations. All we do is specify that we need this particular package, but don't enforce where one gets it from. But we can, and should, document this dependency in the project README.
  
  At this point, the user can manually do:
  `conda install -c vineetbansal -c conda-forge layla`
