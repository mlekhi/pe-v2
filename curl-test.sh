#!/bin/bash

BASE_URL="http://pe-portfolio.duckdns.org:5000/timeline"

create_timeline_post() {
    echo "Creating timeline post..."
    curl -X POST -F "name=Test User" -F "email=test@example.com" -F "content=This is a test post." $BASE_URL/api/timeline_post
}

get_timeline_posts() {
    echo "Getting timeline posts..."
    curl $BASE_URL/api/timeline_post
}

create_timeline_post

get_timeline_posts

echo "Testing complete."

