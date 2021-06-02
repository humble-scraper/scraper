# Old Stuff -- Don't use

`scraper.dockerfile`: An old alpine linux based docker image that I wanted to
use to keep file size down. Ended up going with a selenium base image and then
installing python in that rather than the other way around. I will optimize this
later and create a reduced size docker image because the selenium one is pretty
big.
