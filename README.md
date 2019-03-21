# layla

Boilerplate for a starter Python package meant to go on PyPI or Anaconda Cloud

`setup.py` is heavily commented to point out certain key concepts.


## Testing and building (and re-testing)

1. `conda update conda` and `conda install conda-build` (in base/default environment - conda-build uses the base environment for everything anyway).

1. Create and activate the `build` environment (we'll need `twine` for pypi uploading, and `pytest` for sanity checking)

1. `python setup.py test`

  This runs unit tests from the yet-not-installed source. This works because deep inside `setuptools` we find:

    ```
      with self.project_on_sys_path():
        self.run_tests()
    ```

1. Install (source) distribution

  `python setup.py install`

1. Run tests against the *installed* package.

  `pytest`

This works because `pytest` runs tests in the `tests` folder, but is unable to import our library from the current folder (since it's inside a `src` folder), so is forced to get it from the installed location.

## Uploading to PyPI

1. `python setup.py sdist bdist_wheel`

2. Upload pip installable package on Test PyPi

  `python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

3. Create and activate a barebones `deploy` environment.

   `conda create -n layla_deploy python=3.6`
   
   `conda activate layla_deploy`

   `pip install -i https://test.pypi.org/simple/ layla --no-cache-dir`

This *should* fail, because our package dependes on importlib_resources>=1.0.2, which is not available on Test PyPI (but *is* available on the main PyPI index). So let's install that first and attempt again:

`pip install importlib_resources>=1.0.2`

`pip install -i https://test.pypi.org/simple/ layla --no-cache-dir`


4. If the above cycle worked, upload the package on PyPi

`python -m twine upload dist/*`

## Uploading to Anaconda

1. Update meta.yaml with latest version.

1. We're purposely being verbose in the following command so we can see exactly what's going on.

1. `conda-build . --no-anaconda-upload --output-folder conda_dist`

This *should* fail, because importib_resources>=1.0.2 is not available on Anaconda. The reason `conda-build` even cares about this is because it's trying to create and activate a temporary environment where it can install and test your package. Let's fix this:

  1. `conda config --get channels`
  
     I don't see `conda-forge` listed here, which is expected.
     
  1. `conda config --add channels conda-forge`
  
      `conda config --get channels`
      
      I now see `conda-forge` in the list, but I've added it as the highest-priority channel! We almost never want to do this, otherwise we're opening ourselves up for a lot of pain and confusion when it comes to reproducibility. `conda-forge` should be consulted as a last resort of standard channel(s) fail.

  1. `conda config --remove channels conda-forge`
  
     `conda config --append channels conda-forge`
     
      `conda config --get channels`
      
      Things look better now. `conda-forge` is listed as a lower-priority channel than the default.
      
1. `conda-build . --no-anaconda-upload --output-folder conda_dist`

   This should build fine now. You'll see a bunch of files in `conda_dist`, `noarch/layla-0.1.3-py_0.tar.bz2` is the one we want.
   
1. `anaconda upload conda_dist/noarch/layla-0.1.3-py_0.tar.bz2`

1. Now that the package is built and uploaded, let's not keep the `conda-forge` channel lingering around our environment.

   `conda config --remove channels conda-forge`
   
1. Create and activate a barebones `deploy` environment. Install our package in it
   `conda create -n layla_deploy python=3.6`
   
   `conda activate layla_deploy`
   
   `conda install -c vineetbansal layla`
   
  Again, this complains:
  
  ```
  PackagesNotFoundError: The following packages are not available from current channels:

  - layla -> importlib_resources[version='>=1.0.2']
  ```
   
  As package authors, we **should not** assume the responsibility of installing dependencies from non-standard (yes, even `conda-forge`) locations. All we do is specify that we need this particular package, but not enforce where one gets it from. But we *can*, and *should*, document this tripping point in the project README.
  
  At this point, the user should manually do:
  
  `conda install -c vineetbansal -c conda-forge layla`
