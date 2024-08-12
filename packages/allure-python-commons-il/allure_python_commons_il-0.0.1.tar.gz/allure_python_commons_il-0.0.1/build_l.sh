# del old build
rm -rf build
rm -rf dist
rm -rf aallure_python_commons_il.egg-info
# setuptools
pip3 install setuptools
# twine
pip3 install twine
# build
pip3 install build
# public
pyproject-build && twine upload --skip-existing dist/*