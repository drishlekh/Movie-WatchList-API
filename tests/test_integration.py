import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app, SessionLocal, Movie

client = TestClient(app)

def setup_function():
    # Clean up the test database before each test
    db = SessionLocal()
    db.query(Movie).delete()
    db.commit()
    db.close()

def teardown_function():
    # Clean up after each test
    db = SessionLocal()
    db.query(Movie).delete()
    db.commit()
    db.close()

def test_create_movie_integration():
    response = client.post("/api/movies", json={
        "title": "Test Movie",
        "director": "Test Director",
        "year": 2022,
        "watched": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Movie"
    assert data["director"] == "Test Director"
    assert data["year"] == 2022
    assert data["watched"] is True

def test_read_movies_integration():
    # First, add a movie
    client.post("/api/movies", json={
        "title": "Read Movie",
        "director": "Director",
        "year": 2021,
        "watched": False
    })
    # Now, get all movies
    response = client.get("/api/movies")
    assert response.status_code == 200
    data = response.json()
    assert any(movie["title"] == "Read Movie" for movie in data)

def test_update_movie_integration():
    # Add a movie
    response = client.post("/api/movies", json={
        "title": "Old Title",
        "director": "Old Director",
        "year": 2000,
        "watched": False
    })
    movie_id = response.json()["id"]
    # Update the movie
    response = client.put(f"/api/movies/{movie_id}", json={
        "title": "New Title",
        "director": "New Director",
        "year": 2023,
        "watched": True
    })
    assert response.status_code == 200
    # Check if updated
    response = client.get("/api/movies")
    data = response.json()
    assert any(movie["title"] == "New Title" for movie in data)

def test_delete_movie_integration():
    # Add a movie
    response = client.post("/api/movies", json={
        "title": "Delete Me",
        "director": "Director",
        "year": 2019,
        "watched": False
    })
    movie_id = response.json()["id"]
    # Delete the movie
    response = client.delete(f"/api/movies/{movie_id}")
    assert response.status_code == 200
    # Check if deleted
    response = client.get("/api/movies")
    data = response.json()
    assert not any(movie["id"] == movie_id for movie in data)

def test_update_nonexistent_movie_integration():
    # Try to update a movie that doesn't exist
    response = client.put("/api/movies/99999", json={
        "title": "Doesn't Exist",
        "director": "Nobody",
        "year": 1900,
        "watched": False
    })
    assert response.status_code == 404

def test_delete_nonexistent_movie_integration():
    # Try to delete a movie that doesn't exist
    response = client.delete("/api/movies/99999")
    assert response.status_code == 404