#!/bin/bash

freeze_requirements() {
    pipenv lock -r > requirements.txt
}

build_image() {
    docker build -t humblebundlescraper:latest \
                 -f ./image-building/scraper.dockerfile \
                 --rm \
                 .
}

cleanup() {
    # Requirements file is no longer needed
    rm -f requirements.txt

    # OPTIONAL: clean up docker images
    docker image prune -f
}

main() (
    cd ../
    echo "========= FREEZING REQUIREMENTS ========="
    freeze_requirements
    echo "========= BUILDING IMAGE ========="
    build_image
    echo "========= CLEANING UP TEMPORARY FILES ========="
    cleanup
)

main
