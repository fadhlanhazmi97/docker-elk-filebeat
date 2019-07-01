FROM golang:alpine AS build
RUN apk update && apk add --no-cache build-base git && \
    go get -v -d -u github.com/elastic/beats/filebeat && \
    cd $GOPATH/src/github.com/elastic/beats/filebeat && \
    echo "build" && \
    go build -i

FROM alpine:3.6
WORKDIR /usr/share/filebeat
USER root
COPY --from=build /go/src/github.com/elastic/beats/filebeat/filebeat /usr/share/filebeat/filebeat
COPY filebeat.yml /usr/share/filebeat/filebeat.yml
RUN chown -R root /usr/share/filebeat/ && chmod -R go-w /usr/share/filebeat/
CMD ["./filebeat","-c", "filebeat.yml"]