from setuptools import setup
from setuptools import PEP420PackageFinder, find_packages


MAJOR = 1
MINOR = 1
MICRO = 0

version = f'{MAJOR}.{MINOR}.{MICRO}'

setup(
    name="libsbml-draw",
    version=version,
    # instructions for these arguments is here:
    #   https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files
    package_dir={"": "src/python"},
    packages=['libsbml_draw'],
    package_data={"libsbml_draw": ["*.dll", '*.so', '*.dylib']},
    install_requires=open('requirements.txt').readlines(),
    extras_require={
        "testing": ["nose"],
        "documentation": ["sphinx", "sphinx_rtd_theme", "sphinx-autobuild", "sphinxcontrib-napoleon"],
    },
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering",
    ],
    test_suite="tests",
)

