conda-build . --no-anaconda-upload --output-folder conda_dist
anaconda upload conda_dist/win64/layla-*.tar.gz