FROM python:3.6-alpine AS build
ENV ELASTALERT_URL https://github.com/Yelp/elastalert/archive/master.zip

WORKDIR /opt

RUN apk add --update --no-cache ca-certificates libmagic openssl-dev py3-yaml openssl libffi-dev gcc musl-dev && \
    wget -O elastalert.zip "${ELASTALERT_URL}" && \
    unzip elastalert.zip && \
    rm elastalert.zip && \
    mkdir elastalert-master/rules && \
    pip install -r elastalert-master/requirements.txt && \
    mv e* /opt/elastalert

FROM python:3.6-alpine
RUN apk add --update --no-cache libmagic
COPY --from=build /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=build /opt/elastalert /opt/elastalert
WORKDIR /opt/elastalert
CMD ["python","-m","elastalert.elastalert","--verbose"]