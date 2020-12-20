#!/bin/bash

freeze_requirements() {
    pipenv lock -r > requirements.txt
}

build_image() {
    docker build -t humblebundlescraper:latest \
                 -f "$(realpath $(find ./ -type f -name scraper.dockerfile))" \
                 --rm \  # Removes intermediary <none> images
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
    echo "========= FREEZING REQUIREMENTS ========="
    freeze_requirements
    echo "========= BUILDING IMAGE ========="
    build_image
    echo "========= RUNNING CONTAINER ========="
    run_container
    echo "========= CLEANING UP TEMPORARY FILES ========="
    cleanup
)

main