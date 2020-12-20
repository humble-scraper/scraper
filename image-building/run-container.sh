#!/bin/bash

# !!! This command is just for testing purposes
# !!! The shm (Shared Memory) parameter
r() {
    docker run --shm-size=1024g \
               --rm \
               -it \
               humblebundlescraper \
               bash
}

[[ ${BASH_SOURCE[0]} == $0 ]] && r $@
