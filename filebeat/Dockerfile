FROM golang:alpine AS build
RUN apk update && apk add --no-cache build-base git && \
    export PATH="$GOPATH/bin:$PATH" && \
    go get -v -d -u github.com/elastic/beats/filebeat && \
    cd $GOPATH/src/github.com/elastic/beats/filebeat && \
    echo "build" && \
    go get github.com/magefile/mage && \
    mage build

FROM alpine:3.6
WORKDIR /usr/share/filebeat
USER root
COPY --from=build /go/src/github.com/elastic/beats/filebeat/filebeat /usr/share/filebeat/filebeat
COPY filebeat.yml /usr/share/filebeat/filebeat.yml
CMD ["./filebeat","-e","-c", "filebeat.yml"]