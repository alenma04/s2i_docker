FROM python:3.7

LABEL io.openshift.s2i.scripts-url="image:///s2i/bin"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

RUN mkdir workdir
WORKDIR /workdir

COPY ./s2i/bin/ /s2i/bin

# keep install of seldon-core after the COPY to force re-build of layer
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000