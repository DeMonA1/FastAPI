FROM python:3.12
# set working directory to /usr/src/app
WORKDIR /usr/src/app
# copy the contents of the current local directory into the container's working directory
ADD . /usr/src/app
# run a command
CMD ["python", "1.py"]