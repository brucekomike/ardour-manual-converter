#!/usr/bin/env bash

if [[ -d "manual" ]]; then
    if [[ -d "sphinx-output" ]]; then
        echo "Directory 'sphinx-output' already exists. Skipping creation."
    else
        mkdir sphinx-output
    fi
else
    echo "Directory 'manual' does not exist. Please run get-repo.sh first to clone the repository."
    exit 1
fi


if [[ $(command -v pandoc) ]]; then
    echo "Pandoc is installed."
else
    echo "Pandoc is not installed. Please install it before running this script."
    exit 1
fi

