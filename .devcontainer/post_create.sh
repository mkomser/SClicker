#!/bin/bash

echo "Installing Python dependencies using Poetry"

cd $1
poetry config virtualenvs.in-project true
poetry install

echo "Installing pre-commit hooks"

poetry run pre-commit install --install-hooks

echo "Installation complete."
