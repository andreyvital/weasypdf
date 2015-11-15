FROM debian:jessie

MAINTAINER Andrey K. Vital <andreykvital@gmail.com>

RUN apt-get update && \
  apt-get install -y python-dev python-pip \
  python-lxml libcairo2 libpango1.0-0 \
  libgdk-pixbuf2.0-0 libffi-dev shared-mime-info && \
  pip install --upgrade cffi && \
  pip install WeasyPrint && \
  pip install tornado && \
  apt-get -y purge manpages manpages-dev wget git build-essential && \
  apt-get -y autoremove && apt-get clean autoclean && \
  dpkg --list |grep ^rc |awk '{print $2;}' |xargs dpkg --purge && \
  rm -rf /tmp /var/lib/{apt,dpkg,cache,log} && \
  mkdir /weasypdf

ADD weasypdf.py /weasypdf
EXPOSE 8080

CMD ["python", "/weasypdf/weasypdf.py"]
