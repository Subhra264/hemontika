FROM node:14.17
LABEL org.opencontainers.image.vendor="Abhra303"
LABEL org.opencontainers.image.authors="Abhra303, Subhra264"
LABEL org.opencontainers.image.source ="https://github.com/Abhra303/hemontika.git"
LABEL version="0.1"
LABEL description="It is the dockerfile for front end of hemontika"

ADD . /home/app
WORKDIR /home/app

RUN npm install

CMD [ "npm","start" ]