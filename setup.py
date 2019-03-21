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

    # What does the project *minimally* need to run correctly?

    # Notes
    # -----
    # Whereas install_requires requirements are minimal, requirements files often contain an exhaustive listing of
    # pinned versions for the purpose of achieving repeatable installations of a complete environment.

    # Whereas install_requires requirements are “Abstract”, i.e. not associated with any particular index,
    # requirements files often contain pip options like --index-url or --find-links to make requirements “Concrete”,
    # i.e. associated with a particular index or directory of packages

    install_requires=[
        'importlib_resources>=1.0.2'
    ]
)