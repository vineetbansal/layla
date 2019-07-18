call conda env create -f build-environment.yml
call conda activate layla_build

pip uninstall -y layla

git clean -f -d

python setup.py build --compiler=mingw32
python setup.py bdist_wheel
python setup.py install

python -c "import layla; print(layla.__file__); print(layla.__version__)"
python -c "from layla.mycmodule import Double; print(Double(21))"

python setup.py sdist
call conda deactivate
call conda env remove --name layla_build