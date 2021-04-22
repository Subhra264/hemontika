FROM python

ENV PYTHONUNBUFFERED 1

ADD . /home/backend_server

WORKDIR /home/backend_server
RUN pip install -r requirements.txt && \
    python manage.py collectstatic