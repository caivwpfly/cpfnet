
set -e
export SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)
export COMPILE_FOLDER=${SHELL_FOLDER}/compile_out

echo SHELL_FOLDER
mkdir -p compile_out
cd compile_out
export CPLUS_INCLUDE_PATH="/home/cai/desk/curl-7.78.0/include/"
export LIBRARY_PATH="/home/cai/desk/"
cmake ../

make -j8

${COMPILE_FOLDER}/src/chttp
#./compile_out/src/chttp {dirname $0}

