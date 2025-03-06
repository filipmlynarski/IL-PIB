#!/bin/bash

POST_ID=1  # Change this to the desired post ID
curl -X DELETE http://localhost:8000/api/posts/$POST_ID/ \
  -H "Content-Type: application/json" 