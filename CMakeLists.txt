# CMake -- if these variables don't show-up in the GUI, need to add them and set their values:
#
# LIBSBML_PREFIX, LIBSBML_INCLUDE_DIR
# PYTHON_INCLUDE_DIR
#
# LIBXML2_PATH (needed to parse an SBML file)
# LIBBZ2_PATH, ZLIB_PATH (needed if the SBML file is compressed)
#
# On Windows, also need: LIBICONV_PATH (for unicode), ws2_32.lib (for networking)
#

cmake_minimum_required(VERSION 2.8.12)
project(libsbml_draw)

set(SBNW_MAJOR_VER 1)
set(SBNW_MINOR_VER 0)
set(SBNW_PATCHLEVEL 0)
set(SBNW_VER_STRING "${SBNW_MAJOR_VER}.${SBNW_MINOR_VER}.${SBNW_PATCHLEVEL}")


if(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    set(FPIC_FLAG "-fPIC")
else()
    set(FPIC_FLAG)
endif()

# <pulling in user config from previously external files>

set(SBNW_CLIENT_BUILD 0)
set(SBNW_DEBUG_LEVEL 2 CACHE INTEGER "Verbosity of debug checks, must be greater than zero")

if(${WIN32})
    set(SBNW_WINDOWS_BUILD ON)
    # Internal Options
    set(SBNW_WIN_COPY_DEPS_TO_INSTALL ON CACHE BOOL "When true, libraries that graphfab depends on (libSBML and its dependencies) will be copied to the graphfab installation directory")
else()
    # Internal Options
    set(ENABLE_FULL_RPATH 1 CACHE BOOL "Enable full RPath in generated executable code")
endif()


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
find_package(PythonLibs)
message(STATUS "Using Python include directory ${PYTHON_INCLUDE_DIR}")


# Dependencies

## SBML

find_library(LIBSBML_LIBRARY sbml libsbml HINTS ${LIBSBML_PREFIX}/lib)
find_library(LIBSBML_STATIC_LIBRARY sbml-static REQUIRED libsbml-static HINTS ${LIBSBML_PREFIX}/lib)
find_path(LIBSBML_INCLUDE_DIR sbml/SBMLTypes.h HINTS ${LIBSBML_PREFIX}/include)

message(STATUS "LIBSBML_INCLUDE_DIR ${LIBSBML_INCLUDE_DIR}")
include_directories(${LIBSBML_INCLUDE_DIR})


# Source Code

set(SOURCE_DIR "src/cpp")
include_directories("src/include")

# Set sources for library

set(SOURCES
    src/cpp/SagittariusAssert.c
    src/cpp/SagittariusCommon.cpp
    src/cpp/SagittariusException.cpp
    src/cpp/error.cpp
    src/cpp/tikz.cpp
    src/cpp/io.cpp
    src/cpp/layout.cpp
    src/cpp/arrowhead.cpp
    src/cpp/box.cpp
    src/cpp/canvas.cpp
    src/cpp/fr.cpp
    src/cpp/point.cpp
    src/cpp/cubic.cpp
    src/cpp/geom.cpp
    src/cpp/transform.cpp
    src/cpp/network.cpp
    src/cpp/autolayoutSBML.cpp
    src/cpp/string_helpers.c
    )

set(HEADERS
    src/include/BaseWORDs.h
    src/include/config.h.in
    src/include/Debug.hpp
    src/include/DefaultBool.hpp
    src/include/SagittariusAssert.h
    src/include/SagittariusCommon.h
    src/include/SagittariusConfigure.h
    src/include/SagittariusCore.h
    src/include/SagittariusException.h
    src/include/SagittariusPlatform.h
    src/include/SagittariusPlatformWin.h
    src/include/SagittariusPrefetch.h
    src/include/error.h
    src/include/magick.h
    src/include/io.h
    src/include/layout.h
    src/include/arrowhead.h
    src/include/box.h
    src/include/canvas.h
    src/include/curve.h
    src/include/fr.h
    src/include/layoutall.h
    src/include/point.h
    src/include/allen.h
    src/include/dist.h
    src/include/geom.h
    src/include/min_max.h
    src/include/rand_unif.h
    src/include/round.h
    src/include/sig.h
    src/include/sign_mag.h
    src/include/transform.h
    src/include/network.h
    src/include/autolayoutSBML.h
    src/include/string_helpers.h
    )

configure_file(src/include/config.h.in ../src/include/config.h)

set(SBNW_SOURCES ${SOURCES} )
set(SBNW_HEADERS ${HEADERS} )


# Shared Library

add_library(libsbml_draw SHARED ${SBNW_SOURCES})

set_target_properties(libsbml_draw PROPERTIES COMPILE_DEFINITIONS SBNW_CLIENT_BUILD=0 )


# Link in dependencies - libxml2 libbz2 zdll libiconv Ws2_32

target_link_libraries(libsbml_draw ${LIBSBML_STATIC_LIBRARY} ${LIBXML2_PATH}) 
target_link_libraries(libsbml_draw ${LIBSBML_STATIC_LIBRARY} ${LIBBZ2_PATH}) 
target_link_libraries(libsbml_draw ${LIBSBML_STATIC_LIBRARY} ${ZLIB_PATH}) 
if(${WIN32})
    target_link_libraries(libsbml_draw ${LIBSBML_STATIC_LIBRARY} ${LIBICONV_PATH}) 
    target_link_libraries(libsbml_draw ${LIBSBML_STATIC_LIBRARY} ws2_32.lib) 
endif()


# Static Library

if(BUILD_STATIC_LIB)

    add_library(libsbml_draw_static STATIC ${SBNW_SOURCES})
    set_target_properties(libsbml_draw_static PROPERTIES COMPILE_DEFINITIONS SBNW_CLIENT_BUILD=0 )

    if(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
        set_target_properties(libsbml_draw_static PROPERTIES COMPILE_FLAGS "-fPIC")
    endif()

    # Link in dependencies

    # SBML
    target_link_libraries(libsbml_draw_static ${LIBSBML_STATIC_LIBRARY} ${LIBXML2_PATH})
    target_link_libraries(libsbml_draw_static ${LIBSBML_STATIC_LIBRARY} ${LIBBZ2_PATH}) 
    target_link_libraries(libsbml_draw_static ${LIBSBML_STATIC_LIBRARY} ${ZLIB_PATH}) 
    if(${WIN32})
        target_link_libraries(libsbml_draw_static ${LIBSBML_STATIC_LIBRARY} ${LIBICONV_PATH})
        target_link_libraries(libsbml_draw_static ${LIBSBML_STATIC_LIBRARY} ws2_32.lib) 
    endif()

endif()


# Library dist
install(TARGETS libsbml_draw RUNTIME DESTINATION bin LIBRARY DESTINATION lib ARCHIVE DESTINATION lib)


# Header dist
add_custom_target(headers)
foreach(f ${SBNW_HEADERS})
    add_custom_command(TARGET headers COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_SOURCE_DIR}/${f}
    ${CMAKE_CURRENT_BINARY_DIR}/../include/libsbml_draw/${f})
endforeach()


message(STATUS "PYTHON_VERSION_MAJOR ${PYTHON_VERSION_MAJOR}")


