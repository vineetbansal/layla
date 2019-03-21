from setuptools import setup, find_packages
import mypack


setup(
    name="vineetb_mypack",
    version=mypack.__version__,
    packages=find_packages(),
    package_data={
        'mypack.data': ['*.txt']
    },
    install_requires=[
        'importlib_resources>=1.0.2'
    ]
)