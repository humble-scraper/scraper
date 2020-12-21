#!/bin/bash

DATADIR="$(realpath ~)/Downloads/mongodb/data/"

create_datadir_if_not_there() {
    ! [[ -d ~/Downloads/monogodb/data ]] && mkdir --parents "$DATADIR"
}

r() {
    create_datadir_if_not_there
    docker run -p 27017:27017 \
               -d \
               -v "$DATADIR":/data/db \
               --name mong \
               mongo
}

[[ ${BASH_SOURCE[0]} == $0 ]] && r $@
