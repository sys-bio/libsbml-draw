cmake_minimum_required(VERSION 2.8.12)
project(libsbml_draw)

set(SOURCE_DIR "src/cpp")
include_directories("src/include")

set(SOURCES "${SOURCE_DIR}/math.cpp")


set(TEST_DIR "tests")

set(TESTS ${SOURCES}
    "${TEST_DIR}/test_main.cpp"
    "${TEST_DIR}/test_math.cpp")

# Generate a test executable
include_directories(lib/catch/include src/include)

add_executable("${PROJECT_NAME}_test" ${TESTS})



