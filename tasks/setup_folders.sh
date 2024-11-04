#!/bin/bash

mkdir -p data

if [ ! -f .env ]; then
    cp .env.example .env
    echo "Please update your .env file with your credentials"
fi