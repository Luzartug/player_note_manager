# Player_note_manager

## Description
In this project, we want to create a web application that allows users to create a player and add their own note to the player. The application will use a Flask backend and a PostgreSQL database.

## Installation

### Pull image from docker hub
docker compose up -d html_app

### Build image from Dockerfile
docker compose build

### Run the container
docker compose up html_app

### If you change the app.py file, you need to rebuild the image
docker compose up --build html_app