FROM python:3.9-alpine

# Make a directory for the app
WORKDIR /usr/src/HumbleBundleScraper/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Container command runs the app
CMD ["python", "./App.py"]