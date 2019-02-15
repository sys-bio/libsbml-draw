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
find_package(PythonLibs)
message(STATUS "Using Python include directory ${PYTHON_INCLUDE_DIR}")

# Dependencies

## SBML

find_library(LIBSBML_LIBRARY sbml libsbml HINTS ${LIBSBML_PREFIX}/lib)
find_library(LIBSBML_STATIC_LIBRARY sbml-static REQUIRED libsbml-static HINTS ${LIBSBML_PREFIX}/lib)
find_path(LIBSBML_INCLUDE_DIR sbml/SBMLTypes.h HINTS ${LIBSBML_PREFIX}/include)
#find_path(LIBSBML_EXTRA_LIBS libbz2.lib HINTS ${LIBSBML_PREFIX}/lib)
message(STATUS "LIBSBML_INCLUDE_DIR ${LIBSBML_INCLUDE_DIR}")
include_directories(${LIBSBML_INCLUDE_DIR})

# Image Magick
if(LINK_WITH_MAGICK)
    set(SBNW_USE_MAGICK 1)
    include_directories(${MAGICK_INCLUDE})
else()
    set(SBNW_USE_MAGICK 0)
endif()


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


# Sphinx 

configure_file(docs/source/conf.py docs/source/conf.py)
configure_file(docs/source/index.rst docs/source/index.rst COPYONLY)
configure_file(docs/Makefile docs/Makefile COPYONLY)

# Shared Library

add_library(sbnw SHARED ${SBNW_SOURCES})

set_target_properties(sbnw PROPERTIES COMPILE_DEFINITIONS SBNW_CLIENT_BUILD=0 )

# Link in dependencies

if(LINK_WITH_LIBSBML)
    # libxml2 libbz2 zdll libiconv Ws2_32
    target_link_libraries(sbnw ${LIBSBML_STATIC_LIBRARY} ${LIBXML2_DIR}) 
	target_link_libraries(sbnw ${LIBSBML_STATIC_LIBRARY} ${LIBBZ2_DIR}) 
	target_link_libraries(sbnw ${LIBSBML_STATIC_LIBRARY} ${LIBICONV_DIR}) 
	target_link_libraries(sbnw ${LIBSBML_STATIC_LIBRARY} ${ZLIB_DIR}) 
	target_link_libraries(sbnw ${LIBSBML_STATIC_LIBRARY} ws2_32.lib) 
endif()

# Static Library

if(BUILD_STATIC_LIB)
    add_library(sbnw_static STATIC ${SBNW_SOURCES})
    set_target_properties(sbnw_static PROPERTIES COMPILE_DEFINITIONS SBNW_CLIENT_BUILD=0 )
    if(${CMAKE_SYSTEM_NAME} MATCHES "Windows")
        set_target_properties(sbnw_static PROPERTIES OUTPUT_NAME "libsbnw_static" COMPILE_FLAGS
"/DPY_MAJOR_VERSION=${PYTHON_VERSION_MAJOR}) /DPYTHON_SCREWED_IT_UP=1" PREFIX "" )
    else()
        set_target_properties(sbnw_static PROPERTIES COMPILE_FLAGS "-fPIC")
    endif()

    # Link in dependencies

    # SBML
    target_link_libraries(sbnw_static ${LIBSBML_STATIC_LIBRARY} ${LIBXML2_DIR})
	target_link_libraries(sbnw ${LIBSBML_STATIC_LIBRARY} ${LIBBZ2_DIR}) 
	target_link_libraries(sbnw ${LIBSBML_STATIC_LIBRARY} ${LIBICONV_DIR}) 
	target_link_libraries(sbnw ${LIBSBML_STATIC_LIBRARY} ${ZLIB_DIR}) 
	target_link_libraries(sbnw ${LIBSBML_STATIC_LIBRARY} ws2_32.lib) 

endif()

# Library dist
install(TARGETS libsbml_draw RUNTIME DESTINATION bin LIBRARY DESTINATION lib ARCHIVE DESTINATION lib)

# Header dist
add_custom_target(headers)
foreach(f ${SBNW_HEADERS})
    add_custom_command(TARGET headers COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_SOURCE_DIR}/${f}
    ${CMAKE_CURRENT_BINARY_DIR}/../include/sbnw/${f})
endforeach()

message(STATUS "PYTHON_VERSION_MAJOR ${PYTHON_VERSION_MAJOR}")

# Python


# Doxygen

set(DOXYGEN_OTHER_FILES)
set(SBNW_DOXY_INPUT "")
foreach(f ${HEADERS} ${DOXYGEN_OTHER_FILES})
    set(SBNW_DOXY_INPUT "${SBNW_DOXY_INPUT} ${CMAKE_CURRENT_SOURCE_DIR}/${f}")
endforeach()
configure_file(doxy/doxy.cfg doxy/doxy.cfg)
add_custom_target(docs COMMAND doxygen doxy/doxy.cfg)


