from distutils.core import setup
from setuptools import PEP420PackageFinder

exec(open("src/python/libsbml_draw/version.py").read())

MAJOR = 0
MINOR = 0
MICRO = 0

version = f'{MAJOR}.{MINOR}.{MICRO}'

setup(
    name="libsbml-draw",
    version=version,
    packages=PEP420PackageFinder.find("src/python"),
    package_dir={"": "src/python"},
    package_data={"libsbml_draw.c_api": ["libs/libsbml_draw.dll", "libs/libsbml_draw.dylib", "libs/libsbml_draw.so"],
                  "libsbml_draw.model": ["libs/*.xml"]},
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
