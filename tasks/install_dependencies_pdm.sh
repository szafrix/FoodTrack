#!/bin/bash

if ! command -v pdm &> /dev/null
then
    echo "PDM could not be found. Please install PDM first."
    exit 1
fi

pdm sync

echo "Venv setup & dependencies installed using PDM."