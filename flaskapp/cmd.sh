#!/bin/bash
set -e 
# specify app folder
export FLASK_APP='app'

if [ "$mode" = "DEV" ]; then
  echo "Running App for Development"
  export FLASK_CONFIG='development'
  export FLASK_ENV='development'
  exec flask run --host=0.0.0.0  

elif [ "$mode" = "TEST" ]; then
  echo "Running App for Testing"
  export FLASK_CONFIG='testing'
  exec flask run --host=0.0.0.0
else
  echo "Running Production Server"  
  #exec gunicorn -w 2 -b 0.0.0.0:5000 flaskapp/app:app
fi