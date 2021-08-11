FROM python

LABEL org.opencontainers.image.vendor="Abhra303"
LABEL org.opencontainers.image.authors="Abhra303"
LABEL org.opencontainers.image.source ="https://github.com/Abhra303/hemontika.git"
LABEL version="0.1"
LABEL description="It is the dockerfile for backend_server of hemontika"
ENV PYTHONUNBUFFERED 1

ADD . /home/backend_server

WORKDIR /home/backend_server
RUN pip install -r requirements.txt && \
    python src/manage.py collectstatic