FROM python:3.9-alpine

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.9/main' >> /etc/apk/repositories \
    && echo 'http://dl-cdn.alpinelinux.org/alpine/v3.9/community' >> /etc/apk/repositories \
    && apk update \
    && apk add mongodb yaml-cpp=0.6.2-r2 \
    && mongo -version \
    && mkdir --parents /data/db/ \
    && adduser -D -g '' mongo \
    && chown -R mongo:mongo /data/

USER mongo

CMD ["mongod", "--bind_ip_all"]
