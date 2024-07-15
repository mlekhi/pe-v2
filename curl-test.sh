#!/bin/bash

BASE_URL="http://localhost:5000"

create_timeline_post() {
    echo "Creating timeline post..."
    curl -X POST -F "name=Test User" -F "email=test@example.com" -F "content=This is a test post." $BASE_URL/api/timeline_post
}

get_timeline_posts() {
    echo "Getting timeline posts..."
    curl $BASE_URL/api/timeline_post
}

# Main script flow
echo "Testing Timeline Post Endpoints..."

# Create a timeline post
create_timeline_post

# Get timeline posts to verify
get_timeline_posts

echo "Testing complete."

