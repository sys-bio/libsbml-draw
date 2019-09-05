# libsbml-draw: draws SBML models, generates layouts if desired, allows changing render data

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

Python and C: https://libsbml-draw.readthedocs.io/en/latest/index.html

## How to build the Python documentation

The ReadTheDocs documentation is in the docs directory, and the configuration is specified in the docs/source/conf.py file.

The ReadTheDocs documentation is automatically updated each time a push is made to the libsbml_draw repo.

A link to the C/C++ documentation is located in the docs\source\refmanual\c_api.rst file.

## How to build the C/C++ documentation

The C/C++ documentation is located in the doxy dir of the libsbml-draw repo.

To build the documentation:

1. libsbml-draw> cd doxy
2. libsbml-draw\doxy> doxygen doxy.cfg

By executing the two commands above, the documentation will be generated.  The output directory of this build
is specified in the doxy.cfg file.  Currently, it is set to output to the doxy/build directory.

To update the documentation available online via GitHub Pages:

1. In the libsbml-draw repo, checkout the remote gh-pages branch:

    libsbml-draw> git fetch
    libsbml-draw> git checkout gh-pages

2. verify that you are on the gh-pages branch (the asterisk should be next to gh-pages):
   libsbml-draw> git branch 

3. copy the files in the doxy\build directory to the libsbml-draw directory of the gh-pages branch

4. push the new files
   libsbml-draw> git push

## How to compile the C/C++ SBNW library

 * Install the latest version of <a href="http://sourceforge.net/projects/sbml/files/libsbml/">libSBML</a> or build it from source (tested with 5.6, 5.8, 5.10, 5.11).
   (**VIDEO** showing steps to follow to build from source using CMAKE and Visual Studio: https://www.youtube.com/watch?v=e_Lydwzx-Hg, note that a few steps differ from what is shown in the video:
    specifically, 0) you can download the 64-bit versions if you like; in the video the 32-bit versions are used 
                  1) in CMAKE, you want to set the CMAKE_INSTALL_PREFIX to the INSTALL dir you created in your Visual Studio Project directory 
                  2) in CMAKE, you want to check the box for ENABLE_LAYOUT 
                  3) in Visual Studio, in addition to building the ALL_BUILD target as shown in the video, 
                     you also want to build the INSTALL target
   )  
 * **NOTE**: If you install a pre-built binary of libSBML then you must compile SBNW with the same version of Visual Studio as used to build libSBML.

 * Clone the latest revision of the <a href="https://github.com/sys-bio/sbnw">master branch</a> to Documents\Visual Studio 2017\Projects\sbnw via git. 
   In the Documents\Visual Studio 2017\Projects\ folder, run `git clone https://github.com/sys-bio/sbnw.git`

 * Create BUILD and INSTALL directories in Documents\Visual Studio 2017\Projects\ to hold the build and install files that will be created (the names BUILD and INSTALL are suggestions, not requirements)

 * Download and install <a href="http://www.cmake.org/">CMake</a> (compatible with major version 2 or 3).

 * Open CMake and select Documents\Visual Studio 2017\Projects\sbnw as the source directory.

 * Select Documents\Visual Studio 2017\Projects\BUILD as the build directory.

 * Click on the Advanced option, in the top right section of the main CMake page.

 * Click configure & generate via CMake, choosing a generator that matches the required configuration (32-bit x86 is recommended on Windows; on Linux the default generator is sufficient).

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

 * If you are compiling with Python support, set `PYTHON_EXECUTABLE` to your Python executable, `PYTHON_LIBRARY` to your Python library, and `PYTHON_INCLUDE_DIR` to the Python include directory. Use `SBNW_LINK_TO_STATIC_LIBSBML=ON` if compiling with Python.

 * **NOTE**: In order to statically link to libSBML, specify `SBNW_LINK_TO_STATIC_LIBSBML=ON`. Otherwise, the libSBML DLLs must be in the PATH to run any compiled code.

 * On Windows, open the generated .sln in Visual Studio, and change the configuration to "Release"; on Linux/Mac simply run make -j4 install from the build directory.

 * *(This step was previously used to instruct the user to set the MSVC runtime library. It is now set automatically through CMake. This placeholder serves as a reminder in case this solution breaks at some point.)*

 * **Windows Specific:** In Visual Studio, right click on the INSTALL target and select build. SBNW will be installed to the location stored in CMAKE_INSTALL_PREFIX (ensure your user has write access).


## License

This project is licensed under the MIT License:
