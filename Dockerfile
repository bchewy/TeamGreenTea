FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /TeamGreenTea
WORKDIR /TeamGreenTea
ADD . /TeamGreenTea/
RUN pip install -r requirements.txt