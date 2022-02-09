# Backend Coding Challenge

[![Build Status](https://github.com/Thermondo/backend-code-challenge/actions/workflows/main.yml/badge.svg?event=push)](https://github.com/Thermondo/backend-code-challenge/actions)

Backend REST API for a simple note-taking app.

### Application Features:
* Users can add, delete and modify their notes using django mixins
* Users must be logged in, in order to view/add/delete/etc. their notes using default django 'isauthenticated' and custom made 'isowner' permissions
* Notes can be either public or private - Public notes can be viewed without authentication, however they cannot be modified
* Users can see a list of all their notes using django apiview
* Users can filter their notes via tags
* Search contents of their notes with keywords
* User management API to create new users using default admin panel
* Token based authentication using third party package djangorestframework-simplejwt supported by django

### The model fields:
* id - pk
* title, body, tags - represents notes details
* is_public - represents whether notes made by user is public or private
* owner - represents the creater of the note

### Project Setup
* cd to root folder and run following commands
* Build the docker image with all dependencies installed: docker build -t image_name:tag_name .
* To run the image: docker run image_name:tag_name

### Testing 🚀
* On root folder, run: python manage.py test
