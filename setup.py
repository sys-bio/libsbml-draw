from setuptools import setup, PEP420PackageFinder

setup(
    name="libsbml-draw",
    version="0.0.1",
    packages=PEP420PackageFinder.find("src/python"),
    package_dir={"": "src/python"},
    install_requires=["matplotlib"],
    extras_require={
        "testing": ["pytest", "pytest-mock"],
        "documentation": ["sphinx", "sphinx_rtd_theme", "sphinx-autobuild", "sphinxcontrib-napoleon"],
    },
    zip_safe=False,
    classifiers=[
        "Intendend Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: SystemsBiology",
    ],
)