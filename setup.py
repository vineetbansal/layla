from setuptools import setup, find_namespace_packages, Extension


setup(
    name="layla",
    version="0.5.2",

    package_dir={'': 'src'},

    # The advantage of using `find_namespace_packages` instead of the commonly-used `find_packages` is that
    # the latter will discover a top-level `tests` package, if any, and include it directly in the environment's
    # `site-packages` folder, at the top level, detached from our main package, which is never what we want.
    # This way we are forced to be explicit about whether to include `tests` in our distribution or not.
    packages=find_namespace_packages(where='src'),

    # Should setuptools consult the MANIFEST.in file to see what else needs to be included?
    # Again, this has nothing to do with how we would go about loading it in our code
    # (which is tricky if it cannot be reached through the python package loading mechanism - since the whole
    # source folder might be zipped up, we cannot rely on os.path etc. mechanisms)
    # This is where importlib_resources>=1.0.2 comes in
    include_package_data=True,

    # What does the project *minimally* need to run correctly?

    # Notes
    # -----
    # Whereas install_requires requirements are minimal, requirements files often contain an exhaustive listing of
    # pinned versions for the purpose of achieving repeatable installations of a complete environment.

    install_requires=[
        'importlib_resources>=1.0.2'
    ],

    # For this to work without a lot of fuss, make sure that 'tests' is a package by including an __init__.py
    test_suite='tests',

    # C extensions as submodules of the main package
    ext_modules=[
        Extension(
            'layla.mycmodule',
            sources=['_cextension/c_extension.cpp'],
            include_dirs=['_cextension/include'],
            library_dirs=['_cextension/lib'],
            libraries=['example_dll'],
            extra_compile_args=['-D_hypot=hypot', '-DMS_WIN64']
        )
    ],

    zip_safe=False

)


