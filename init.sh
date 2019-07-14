#!/bin/ash
cd /app-run/app

echo "INSTALLING magneto.app:"
pip install .
echo "TESTING magneto.app:"
py.test --cov=magneto /app-run/app/tests

cd /run-app/

gunicorn -w 4 --bind 0.0.0.0:5000 --chdir /app-run/api/ server:app --reload