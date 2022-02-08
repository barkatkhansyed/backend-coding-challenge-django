# Backend Coding Challenge

[![Build Status](https://github.com/Thermondo/backend-code-challenge/actions/workflows/main.yml/badge.svg?event=push)](https://github.com/Thermondo/backend-code-challenge/actions)

Backend REST API for a simple note-taking app.

### Application Features:
* Users can add, delete and modify their notes using django mixins
* Users can see a list of all their notes using django apiview
* Users can filter their notes via tags
* Users must be logged in, in order to view/add/delete/etc. their notes using default django 'isauthenticated' and custom made 'isowner' permissions
* Search contents of their notes with keywords
* Notes can be either public or private - Public notes can be viewed without authentication, however they cannot be modified
* User management API to create new users using default admin panel
* Token based authentication using jwt

### The model fields:
* id - pk
* title, body, tags - represents note details
* is_public - represents whether note made by user is public or private
* owner - represents the creater of the note

### Testing 🚀

