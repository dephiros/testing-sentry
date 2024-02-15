#!/usr/bin/env bash

# exit on first error
set -xe

# create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install (or update) requirements
python -m pip install -r requirements.txt

# Initialize database
# flask --app flaskr init-db

# Run Flask application on localhost:5000
flask --app flaskr run