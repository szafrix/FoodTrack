#!/bin/bash

if [ "$1" = "pip" ]; then
    ./tasks/install_dependencies_pip.sh
elif [ "$1" = "pdm" ]; then
    ./tasks/install_dependencies_pdm.sh
else
    echo "Error: Invalid installation method. Please use 'pip' or 'pdm' as argument"
    exit 1
fi