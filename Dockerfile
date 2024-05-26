FROM python:3.10-alpine

ENV FLASK_APP filme

RUN adduser -D filme

USER filme

WORKDIR /home/filme/

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY filme.py filme.py


RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt

EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
