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

1. Update meta.yaml with latest .tar.gz link and sha256 checksum.
1. Update version no. in meta.yaml
1. conda config --get channels
1. conda config --add channels conda-forge 
1. conda config --get channels # oops, we wanted lowest priority for conda-forge
1. conda config --remove channels conda-forge
1. conda config --append channels conda-forge
1. conda build .
1. anaconda upload c:\ProgramData\Anaconda3\conda-bld\noarch\vineetb-mypack-0.1.3-py_0.tar.bz2
1. 8. conda config --remove channels conda-forge
1. Create a new conda environment
1. Install our package in it - conda install -c aspyre vineetb-mypack 
1. Why didn't it complain about importlib_resources ??
