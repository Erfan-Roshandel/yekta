#!/bin/bash
# build_and_run.sh

# Build the Docker image
docker build -t email-classifier .

# Run the container
docker run -d \
  --name email-classifier \
  -p 8000:8000 \
  --restart unless-stopped \
  email-classifier

echo "Application is running at http://localhost:8000/docs"