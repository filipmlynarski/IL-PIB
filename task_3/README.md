# Post Management REST API

This is a Django REST Framework application that provides an API for managing posts with history tracking and IP-based authorization.

## Features

- Create, read, update, and delete posts
- Automatic tracking of post history
- IP-based authorization (only creator can modify their posts)
- Keyword validation (minimum 3 unique keywords required)
- URL validation
- Complete history of all changes

## Requirements

- Python 3.8+
- Django 4.2+
- Django REST Framework 3.14+

## Run

- `python manage.py migrate`
- `python manage.py runserver`

## API Usage

The repository includes several shell scripts to interact with the API:

- `create_post.sh` - Create a new post
- `get_posts.sh` - List all posts
- `update_post.sh` - Update an existing post
- `delete_post.sh` - Delete a post
- `get_history.sh` - View change history
