

cmake_minimum_required(VERSION 3.5)

project(chttp)

############################################################
# Create a library
############################################################

include_directories(${CMAKE_SOURCE_DIR}/include)
aux_source_directory(. SRC)
#target_include_directories(${PROJECT} ${PROJECT_SOURCE_DIR}/include)

############################################################
# Create an executable
############################################################

# Add an executable with the above sources
add_executable(${PROJECT_NAME} ${SRC})

# link the new hello_library target with the hello_binary target
target_link_libraries(${PROJECT_NAME} PUBLIC curl)