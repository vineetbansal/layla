1. python setup.py sdist bdist_wheel
2. python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
3. Update meta.yaml with latest .tar.gz link and sha256 checksum.
4. Update version no. in meta.yaml
5. conda config --get channels
6. conda config --add channels conda-forge 
7. conda config --get channels # oops, we wanted lowest priority for conda-forge
8. conda config --remove channels conda-forge
9. conda config --append channels conda-forge
10. conda build .
11. anaconda upload c:\ProgramData\Anaconda3\conda-bld\noarch\vineetb-mypack-0.1.3-py_0.tar.bz2
12. 8. conda config --remove channels conda-forge
13. Create a new conda environment
14. Install our package in it - conda install -c aspyre vineetb-mypack 
15. Why didn't it complain about importlib_resources ??