#!/bin/bash

# This file can be used for setting up non-secret env vars. Ideally, you should do:
#   1. Make a file called `.env`
#   2. Place your environmment variables in there

echo "Exporting environmnet variables..."

# URL for the mongodb database
export DB_URL=""

# Scraping speed in ms (time between waits)
export SCRAPING_SPEED="1000"