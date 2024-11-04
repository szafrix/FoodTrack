#!/bin/bash

if ! command -v virtualenv &> /dev/null
then
    echo "virtualenv could not be found, use `pip install virtualenv` first"
    exit 1
fi

if [ ! -d "venv" ]; then
    virtualenv venv
fi

source venv/bin/activate
pip install -r requirements.txt

echo "Venv setup & dependencies installed using pip."