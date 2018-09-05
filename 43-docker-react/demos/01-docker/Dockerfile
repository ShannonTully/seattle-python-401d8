FROM python:3
RUN apt-get update
RUN apt-get upgrade -y
EXPOSE 8080
WORKDIR ./usr/src
COPY myapp.py /usr/src
CMD python /usr/src/myapp.py

