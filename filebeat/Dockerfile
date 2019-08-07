FROM golang:alpine AS build
ARG version
RUN apk update && apk add --no-cache build-base git && \
    export PATH="$GOPATH/bin:$PATH" && \
    go get -v -d -u github.com/elastic/beats/filebeat && \
    cd $GOPATH/src/github.com/elastic/beats/filebeat && \
    git checkout $version && \
    echo "build" && \
    go get github.com/magefile/mage && \
    mage build && ./filebeat version && \
    mkdir compiled && \
    mv filebeat compiled/filebeat && \
    mv module compiled/module && mv modules.d compiled/modules.d

FROM alpine:3.6
WORKDIR /usr/share/filebeat
USER root
COPY --from=build /go/src/github.com/elastic/beats/filebeat/compiled /usr/share/filebeat/
CMD ["./filebeat","-strict.perms=false","-e","-c", "filebeat.yml"]