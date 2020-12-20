FROM selenium/standalone-chrome

USER root

# Make a directory for the app
WORKDIR /usr/src/HumbleBundleScraper/app

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Install dependencies
COPY core/*.py ./core/
COPY requirements.txt App.py ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Container command runs the app
CMD ["python", "./App.py"]