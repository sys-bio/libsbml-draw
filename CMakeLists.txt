cmake_minimum_required(VERSION 2.8.12)
project(libsbml_draw)

set(SBNW_MAJOR_VER 1)
set(SBNW_MINOR_VER 3)
set(SBNW_PATCHLEVEL 27)
set(SBNW_VER_STRING "${SBNW_MAJOR_VER}.${SBNW_MINOR_VER}.${SBNW_PATCHLEVEL}")

set(LINK_WITH_LIBSBML ON)
set(SBNW_LINK_TO_STATIC_LIBSBML ON)

if(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    set(FPIC_FLAG "-fPIC")
else()
    set(FPIC_FLAG)
endif()

# User Configuration
if(${WIN32})
    include( "UserConfigWin.txt" )
else()
    include( "UserConfigLinux.txt" )
endif()

set(SBNW_SPYDER_DIST ON CACHE BOOL "Install Spyder plugin files")
set(BUILD_STATIC_LIB ON CACHE BOOL "Build the static version of the library")

set(ENABLE_PYTHON FALSE CACHE BOOL "Enable Python bindings")
if(ENABLE_PYTHON)
    find_package(PythonInterp)
    if(PYTHONINTERP_FOUND)
        set(Python_ADDITIONAL_VERSIONS ${PYTHON_VERSION_STRING})
    else()
        message(ERROR FATAL "Unable to find Python")
    endif()
endif()

# Find Python Libs
find_pacakge(PythonLibs)
message(STATUS "Using Python include directory ${PYTHON_INCLUDE_DIR}")

# Dependencies

# SBML


set(SOURCE_DIR "src/cpp")
include_directories("src/include")





