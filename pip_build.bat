pip uninstall -y layla

rmdir dist /s /q
rmdir build /s /q
rmdir layla/src/layla.egg-info /s /q

python setup.py build --compiler=mingw32
python setup.py install
python -c "import layla; print(layla.__file__); print(layla.__version__)"
python -c "from layla.mycmodule import Double; print(Double(21))"