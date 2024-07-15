#!/bin/bash

BASE_URL="http://pe-portfolio.duckdns.org:5000/timeline"

echo "Test 1: Creating timeline post..."
curl --request POST "${BASE_URL}" \
     --data-urlencode "name=Wei" \
     --data-urlencode "email=wei.he@mlh.io" \
     --data-urlencode "content=Just Added Database to my portfolio site!"

echo

# Test 2: POST request to create another timeline post
echo "Test 2: Creating another timeline post..."
curl --request POST "${BASE_URL}" \
     --data-urlencode "name=Wei" \
     --data-urlencode "email=wei.he@mlh.io" \
     --data-urlencode "content=Testing my endpoints with postman and curl."

echo
