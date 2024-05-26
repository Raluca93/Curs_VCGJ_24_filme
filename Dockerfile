FROM python:3.10-alpine

ENV FLASK_APP filme
#ENV FLASK_CONFIG = docker

#3.8 booster
#RUN useradd -rm -d /home/site -s /bin/bash -g root -G sudo -u 1001 site

#3.8 alpine
RUN adduser -D filme

USER filme

WORKDIR /home/filme/

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY filme.py filme.py
COPY templates templates
COPY static static



RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt

#WORKDIR /home/sysinfo/app

# runtime configuration
EXPOSE 5000
ENTRYPOINT ["./dockerstart.sh"]
