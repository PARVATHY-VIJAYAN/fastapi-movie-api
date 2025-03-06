# fastapi-movie-api
A simple RESTful API built using FastAPI to perform CRUD operations on a movie collection. This project demonstrates API request handling, response management, and interaction using Python's requests module.

## API Endpoints
GET /movies → Get all movies
GET /movies/{id} → Get a specific movie
POST /movies → Add a new movie
PUT /movies/{id} → Update a movie
DELETE /movies/{id} → Delete a movie

This exercise implements CRUD operations for a movie collection using a dictionary as an in-memory data store. Also, this makes clear that the URL structure defines the resource (e.g., /movies for a collection and /movies/{id} for a specific item), while the HTTP method (GET, POST, PUT, DELETE) determines the action performed on that resource in a RESTful Web application.
