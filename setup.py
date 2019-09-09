from setuptools import setup, PEP420PackageFinder

exec(open("src/python/libsbml_draw/version.py").read())

setup(
    name="libsbml-draw",
    version=__version__,
    packages=PEP420PackageFinder.find("src/python"),
    package_dir={"": "src/python"},
    package_data={"libsbml_draw.c_api": ["data/sbml_draw.dll", "data/libsbml_draw.dylib", "data/libsbml_draw.so"],
                  "libsbml_draw.model": ["data/*.xml"]},
    install_requires=["matplotlib", "numpy", "tesbml>=5.18.0"],
    extras_require={
        "testing": ["pytest", "pytest-mock"],
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
