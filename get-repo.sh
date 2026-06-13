#!/usr/bin/env bash
if [ -d "./manual" ]; then
    echo "Directory 'manual' already exists. Skipping download."
    cd manual
    git pull
    cd ..
else
    git clone https://github.com/ardour/manual.git
fi