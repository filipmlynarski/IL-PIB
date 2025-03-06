#!/bin/bash

POST_ID=1  # Change this to the desired post ID
curl -X PUT http://localhost:8000/api/posts/$POST_ID/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Post Title",
    "description": "This is an updated description for the example post",
    "keywords": "updated post, test content, modified topic",
    "url": "https://example.com/updated-post"
  }' 