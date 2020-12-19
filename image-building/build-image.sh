#!/bin/bash

freeze_requirements() {
    pipenv lock -r > requirements.txt
}

build_image() {
    docker build -t humblebundlescraper \
                 -f "$(realpath $(find ./ -type f -name scraper.dockerfile))" \
                 .
}

# TODO: implement the run_container function
run_container() {
    echo "TODO: Implement the run_container function"
}

cleanup() {

    # Requirements file is no longer needed
    rm -f requirements.txt
}

main() (
    cd ../
    freeze_requirements
    build_image
    run_container
    cleanup
)

main