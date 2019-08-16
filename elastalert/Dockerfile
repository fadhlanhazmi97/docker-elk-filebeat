FROM alpine:latest AS build
ENV ELASTALERT_URL https://github.com/Yelp/elastalert/archive/master.zip

WORKDIR /opt

RUN apk add --update --no-cache ca-certificates openssl-dev openssl python3-dev=3.6 python3=3.6 py3-pip py3-yaml libffi-dev gcc musl-dev && \
    wget -O elastalert.zip "${ELASTALERT_URL}" && \
    unzip elastalert.zip && \
    rm elastalert.zip && \
    mkdir elastalert-master/rules && \
    pip3 install -r elastalert-master/requirements.txt && \
    mv e* /opt/elastalert

FROM alpine:latest

RUN apk add --update --no-cache python3 libmagic
COPY --from=build /usr/lib/python3.7/site-packages /usr/lib/python3.7/site-packages
COPY --from=build /opt/elastalert /opt/elastalert

WORKDIR /opt/elastalert

CMD ["python3","-m","elastalert.elastalert","--verbose"]