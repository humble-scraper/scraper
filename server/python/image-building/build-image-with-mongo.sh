#!/bin/bash

build-image() {
    docker build -t humblemongo:latest -f mongo-alpine-python.dockerfile .
}

run-container() {
    docker run -d --name humble-test -p 27018:27017 humblemongo
}

r() {
    build-image
    run-container
}

[[ ${BASH_SOURCE[0]} == $0 ]] && r $@
