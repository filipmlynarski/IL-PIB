#!/bin/bash

curl -X POST http://localhost:8000/api/posts/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Example Post",
    "description": "This is an example post describing something interesting",
    "keywords": "example post, test content, interesting topic",
    "url": "https://example.com/post1"
  }' 