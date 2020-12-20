FROM python:3.9-alpine

# Make a directory for the app
WORKDIR /usr/src/HumbleBundleScraper/app

# Install dependencies
COPY lib/ ./lib/
COPY core/*.py ./core/
COPY requirements.txt App.py ./
RUN pip install --no-cache-dir -r requirements.txt

# Install latest Chromium
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" > /etc/apk/repositories \
    && echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
    && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
    && echo "http://dl-cdn.alpinelinux.org/alpine/v3.12/main" >> /etc/apk/repositories \
    && apk upgrade -U -a \
    && apk add \
    libstdc++ \
    chromium \
    harfbuzz \
    nss \
    freetype \
    ttf-freefont \
    font-noto-emoji \
    wqy-zenhei \
    && rm -rf /var/cache/* \
    && mkdir /var/cache/apk

# Container command runs the app
CMD ["python", "./App.py"]