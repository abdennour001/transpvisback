FROM python:3

# install sudo
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*

# install postgresql for backups
RUN sudo apt-get update && apt-get install -y lsb-release && apt-get clean all
RUN sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
RUN sudo apt-get -qq update
RUN sudo apt-get install postgresql-client-12 -y

# create and define workdir
RUN mkdir /code
WORKDIR /code

# add and install requirements
ADD requirements.txt /code/
RUN pip install -r requirements.txt

# move code from host to image
ADD . /code/