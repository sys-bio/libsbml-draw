# libsbml-draw: 

### SBML viewer, layout generator, render style editor

## Introduction

The SBML layout and render extensions enable SBML models to encode 
information about the graphical depiction of model elements. 
Layout provides information about the positions of model elements 
and render describes the styles of elements, for example, shapes, 
colors, line widths, and font details.

libsbml_draw supports the SBML layout and render extensions and can 
automatically generate a layout for SBML models by making use of SBNW, 
a C/C++ library.

## Documentation

Python and C/C++: https://libsbml-draw.readthedocs.io/en/latest/index.html

## Installation Instructions For Using libsbml-draw With "Tellurium For Windows"

1. First, you will need a version of Tellurium >= Tellurium-2.1.8-Python-3.7

   * If you already have an earlier version of Tellurium installed on Windows, uninstall it.  

    This can be done by finding Tellurium on the Windows menu, 
    clicking on the dropdown arrow, and choosing the "Uninstall Tellurium" option.

   * You can find the necessary version of Tellurium at:    
    https://sourceforge.net/projects/pytellurium/

    Download the executable file (*setup.exe) and run it to install Tellurium.

2. Next, install libsbml-draw using the Python provided by Tellurium:

    The location of this Python depends on where you installed Tellurium.  
    
    It could be something like: `C:\Tellurium-Winpython-3.7\python-3.7.4.amd64\python.exe`

    Open a Windows terminal, and install 'libsbml-draw':

    `C:\Users\UserX> <path to your Tellurium python>\python.exe -m pip install libsbml-draw`  
       
## Installation Instructions for Using libsbml-draw outside of "Tellurium for Windows"

1. You can install `libsbml-draw` using pip, either as part of your base system of site-packages, 
   or within a Python environment, using:

    `pip install libsbml-draw`

2. If you want to use `tellurium` packages along with it, you can install tellurium:

    `pip install tellurium`

   Note: `libsbml-draw` depends on the `tesbml` package >= version 5.18.1 for `libsbml`. 

## How to create a distribution package for libsbml-draw; i.e. archives that can be uploaded to the Package Index and installed by pip

0. Increment the version number, which can be found in the `libsbml-draw\src\python\libsbml_draw\version.py` file in the `libsbml-draw` repo.

1. Make sure you have the latest versions of setuptools and wheel installed:

	`python3 -m pip install --user --upgrade setuptools wheel`

2. Run this command from the same directory where `setup.py` is located in the `libsbml-draw` repo:

	`python3 setup.py sdist bdist_wheel`

3. This command should output a lot of text and once completed should generate two files in the `dist` directory of the `libsbml-draw` repo:

	dist/  
	    libsbml-draw-0.0.x.tar.gz  
	    libsbml_draw-0.0.x-py3-none-any.whl  

The `tar.gz` file is a source archive whereas the `.whl` file is a built distribution.  Newer pip versions preferentially install built
distributions, but will fall back to source archives if needed.  `libsbml-draw` is compatible with Python on any platform so only one
built distribution is needed.

## How to upload distribution archives to Test PyPI

1. Register an account on Test PyPI, https://test.pypi.org/account/register 

   Test PyPI is a separate instance of the package index intended for testing and experimentation.

2. You can use twine to upload the distribution packages.  You will need to install twine:

	`python3 -m pip install --user --upgrade twine`

3. Once installed, run twine to upload all of the archives under dist:

	`python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

   You will be prompted for the username and password you registered with Test PyPI.  

4. Once uploaded the package should be viewable on TestPyPI, for example, 
   
	https://test.pypi.org/project/libsbml-draw/

## Installing the newly uploaded package

1. Pip can be used to install the package

	`python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps libsbml-draw`

   pip should install the package from Test PyPI.

   The command above specifies --no-deps.  Since TestPyPI doesn't have the same pacakges as
   the live PyPI, it's possible that attempting to install dependencies may fail or install 
   something unexpected.  It's a good practice to avoid installing dependencies when using
   TestPyPI.

## How to upload distribution archives to PyPI

1. Register an account PyPI, https://pypi.org/account/register 

   PyPI is the real deal.

2. You can use twine to upload the distribution packages.  You will need to install twine:

	`python3 -m pip install --user --upgrade twine`

3. Once installed, run twine to upload all of the archives under dist:

	`python3 -m twine upload dist/*`

   You will be prompted for the username and password you registered with PyPI.  

4. Once uploaded the package should be viewable on PyPI, for example, 

        https://pypi.org/project/libsbml-draw/

## How to build the Python documentation

The ReadTheDocs documentation is in the `docs` directory of the `libsbml-draw` repo, and the configuration 
is specified in the `docs/source/conf.py` file.  The `conf.py` file is configured such that documentation from 
the project's  `.py` files is automatically generated.  `.rst` files specify the structure of the documentation
displayed on ReadTheDocs.

The ReadTheDocs documentation is automatically updated each time a push is made to the `libsbml-draw` repo.

A link to the C/C++ documentation is located in the `docs\source\refmanual\c_api.rst` file.

## How to build the C/C++ documentation

The C/C++ documentation is located in the `doxy` dir of the libsbml-draw repo.  GitHub pages are used to make the
documentation available online (Note: The ReadTheDocs documentation for libsbml-draw contains a link to this C/C++ documentation.).  
To make this work, a `gh-pages branch` of the `libsbml-draw` repo was created.  

To build the documentation:

1. In the libsbml-draw repo, checkout the `remote gh-pages branch`:

	`libsbml-draw> git fetch origin`  
	`libsbml-draw> git checkout -b gh-pages origin/gh-pages`  

2. Verify that you are on the gh-pages branch (the asterisk should be next to gh-pages):

	`libsbml-draw> git branch -a`

3. Generate a new version of the documentation by cd'ing into the directory containing the C/C++ documentation and executing the `doxygen` command:

	`libsbml-draw> cd doxy`
   	`libsbml-draw\doxy> doxygen doxy.cfg`

  By executing the two commands above, the documentation will be generated.  The output directory of this build
  is specified in the `doxy.cfg` file.  Currently, it is set to output to the `doxy/build` directory.

4. In order for these documentation files to appear online, they need to be copied to the root directory of gh-pages branch of the libsbml-draw repo:

   'libsbml-draw\doxy> cd build'
   'libsbml-draw\doxy\build> copy * ..\..\.`

5. push the new files to the `gh-pages` branch of the `libsbml-draw` repo:

	`libsbml-draw> git push`

## How to compile the C/C++ SBNW library

 * Build the latest version of <a href="http://sourceforge.net/projects/sbml/files/libsbml/">libSBML</a> from source.

   There is a **VIDEO** which shows the steps to follow to build from source using CMAKE and Visual Studio: 

    https://www.youtube.com/watch?v=e_Lydwzx-Hg, note that a few steps differ from what is shown in the video:

    1. You can download the 64-bit versions if you like; in the video the 32-bit versions are used 

    2. In CMAKE, you want to set the CMAKE_INSTALL_PREFIX to the INSTALL dir you created in your Visual Studio Project directory 

    3. In CMAKE, you want to check the box for ENABLE_LAYOUT and ENABLE_RENDER

    4. In Visual Studio, in addition to building the ALL_BUILD target as shown in the video, you also want to build the INSTALL target

 * Clone the latest revision of the <a href="https://github.com/sys-bio/libsbml-draw">master branch</a> to Documents\Visual Studio 2017\Projects\libsbml-draw via git. 
   In the Documents\Visual Studio 2017\Projects\ folder, run `git clone https://github.com/sys-bio/libsbml-draw.git`

 * Create BUILD and INSTALL directories in Documents\Visual Studio 2017\Projects\ to hold the build and install files that will be created (the names BUILD and INSTALL are suggestions, not requirements)

 * Download and install <a href="http://www.cmake.org/">CMake</a> (compatible with major version 2 or 3).

 * Open CMake and select Documents\Visual Studio 2017\Projects\libsbml-draw as the source directory.

 * Select Documents\Visual Studio 2017\Projects\BUILD as the build directory.

 * Click on the Advanced option, in the top right section of the main CMake page.

 * Click configure & generate via CMake, choosing a generator that matches the required configuration.

 * In CMake, if you don't see LIBSBML_PREFIX on the list, click on the +AddEntry button in the top right corner and add it.
   Set the `LIBSBML_PREFIX` variable to point to the directory where libSBML is installed/downloaded. 

 * If libSBML was compiled with compression support, `LIBSBML_EXTRA_LIBS` needs to be set.  If it is not on the list, click on the +AddEntry button in the top right corner and add it.
   Set `LIBSBML_EXTRA_LIBS` to include libxml2, libbz2, and libz. 
   On Linux and Mac, this is `LIBSBML_EXTRA_LIBS='xml2;bz2;z'`. 
   On Windows, you must specify the full path to each dependency in the libSBML third party install folder,    
   e.g. `LIBSBML_EXTRA_LIBS="\path\to\Documents\Visual Studio 2017\Projects\libSBML-5.17.0-Source\INSTALL\lib\libbz2.lib;
        path\to\Documents\Visual Studio 2017\Projects\libSBML-5.17.0-Source\INSTALL\lib\libiconv.lib;
        path\to\Documents\Visual Studio 2017\Projects\libSBML-5.17.0-Source\INSTALL\lib\libxml2.lib;
        path\to\Documents\Visual Studio 2017\Projects\libSBML-5.17.0-Source\INSTALL\lib\zdll.lib;
        ws2_32.lib"'.
   Click configure & generate again.

 * If you are compiling with Python support, set `PYTHON_EXECUTABLE` to your Python executable, `PYTHON_LIBRARY` to your Python library, and `PYTHON_INCLUDE_DIR` to the Python include directory. 
   Use `SBNW_LINK_TO_STATIC_LIBSBML=ON` if compiling with Python.

 * **NOTE**: In order to statically link to libSBML, specify `SBNW_LINK_TO_STATIC_LIBSBML=ON`. Otherwise, the libSBML DLLs must be in the PATH to run any compiled code.

 * On Windows, open the generated .sln in Visual Studio, and change the configuration to "Release"; on Linux/Mac simply run make -j4 install from the build directory.

 * **Windows Specific:** In Visual Studio, right click on the INSTALL target and select build. libsbml-draw will be installed to the location stored in CMAKE_INSTALL_PREFIX.

 * **Notes on the build process** also exist in the `libsbml-draw` repo in the directory, `libsbml-draw/install_notes`

## License

This project is licensed under the MIT License:

Copyright (c) 2019 Sauro Lab, UW Bioengineering

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
