#!/bin/bash

BASE_URL="http://localhost:5000"

create_timeline_post() {
    curl -X POST -F "name=Test User" -F "email=test@example.com" -F "content=This is a test post." $BASE_URL/api/timeline_post
}

get_timeline_posts() {
    curl $BASE_URL/api/timeline_post
}

delete_timeline_post() {
    curl -X DELETE $BASE_URL/api/timeline_post/{post_id}
}

create_timeline_post
get_timeline_posts
# delete_timeline_post
