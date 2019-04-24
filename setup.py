from setuptools import setup, PEP420PackageFinder

setup(
    name="libsbml-draw",
    version="0.0.4",
    packages=PEP420PackageFinder.find("src/python"),
    package_dir={"": "src/python"},
    package_data={"libsbml_draw.c_api": ["data/sbnw.dll", "data/libsbml_draw.dylib", "data/libsbml_draw.so"]},
    install_requires=["matplotlib", "numpy", "python-libsbml"],
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
