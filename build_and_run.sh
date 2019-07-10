#!/usr/bin/bash
# For development only, builds the image and mounts flaskapp folder
docker build -t template:beta .
docker run -it -v "$(pwd)/flaskapp":/app -p 5000:5000 --env-file .env --env mode='DEV' template:beta