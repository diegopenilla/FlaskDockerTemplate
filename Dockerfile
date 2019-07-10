# build image:
FROM python:3.7 as builder
RUN mkdir /install
WORKDIR /install
RUN pip install --install-option="--prefix=/install" pipenv

# final image: if slim does not work change it to python:3.7
FROM python:3.7-slim
RUN apt-get update 
# getting requirements from base image
COPY --from=builder /install /usr/local
# copying source files into app folder of container
COPY ["Pipfile", "Pipfile.lock", "ospackages.txt", "./"] 
# install system dependencies from ospackages.txt
RUN cat ospackages.txt | xargs apt-get install -y
# installing requirements.txt with pipenv
RUN pipenv install --system --deploy
# To run Flask in debug or gunicorn in production
COPY ./flaskapp /app
WORKDIR /app
CMD ["./cmd.sh"]

