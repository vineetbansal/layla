pip uninstall -y layla

git clean -f -d

python setup.py build --compiler=mingw32
python setup.py bdist_wheel
python setup.py install

python -c "import layla; print(layla.__file__); print(layla.__version__)"
python -c "from layla.mycmodule import Double; print(Double(21))"