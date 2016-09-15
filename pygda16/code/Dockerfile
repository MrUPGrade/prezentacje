FROM centos:7

MAINTAINER itsupgradetime@gmail.com

RUN yum -y install epel-release && \
    yum -y install python-pip && \
    pip install cherrypy ulog==0.2.0

VOLUME /src
WORKDIR /src

EXPOSE 8080

ADD simple.py /src/simple.py

CMD ["python", "simple.py"]
