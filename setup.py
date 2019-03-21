from setuptools import setup, find_packages
import layla


setup(
    name="layla",
    version=layla.__version__,
    packages=find_packages(),

    # For including non-source files, specify the wildcard path here
    # The key is the package name though, so in this case the layla/data/ folder needs an __init__.py
    # Simply including the file says nothing about how we're going to load it though
    # (which is where importlib_resources>=1.0.2 comes in)
    package_data={
        'layla.data': ['*.txt']
    },

    # Should setuptools consult the MANIFEST.in file to see what else needs to be included?
    # Again, this has nothing to do with how we would go about loading it in our code
    # (which is tricky if it cannot be reached through the python package loading mechanism - since the whole
    # source folder might be zipped up, we cannot rely on os.path etc. mechanisms)
    include_package_data=True,

    # What does the project *minimally* need to run correctly?

    # Notes
    # -----
    # Whereas install_requires requirements are minimal, requirements files often contain an exhaustive listing of
    # pinned versions for the purpose of achieving repeatable installations of a complete environment.

    install_requires=[
        'importlib_resources>=1.0.2'
    ]
)