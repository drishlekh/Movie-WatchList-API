import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_api_get_movies():
    response = client.get("/api/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_api_add_movie():
    response = client.post("/api/movies", json={
        "title": "API Test Movie",
        "director": "API Director",
        "year": 2024,
        "watched": False
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "API Test Movie"
    assert data["director"] == "API Director"
    assert data["year"] == 2024
    assert data["watched"] is False

def test_api_update_movie():
    # First, add a movie to update
    response = client.post("/api/movies", json={
        "title": "To Update",
        "director": "Updater",
        "year": 2020,
        "watched": False
    })
    movie_id = response.json()["id"]
    # Now, update it
    response = client.put(f"/api/movies/{movie_id}", json={
        "title": "Updated Title",
        "director": "Updated Director",
        "year": 2021,
        "watched": True
    })
    assert response.status_code == 200
    # Optionally, check the updated data
    response = client.get("/api/movies")
    movies = response.json()
    assert any(m["title"] == "Updated Title" for m in movies)

def test_api_delete_movie():
    # First, add a movie to delete
    response = client.post("/api/movies", json={
        "title": "To Delete",
        "director": "Deleter",
        "year": 2018,
        "watched": False
    })
    movie_id = response.json()["id"]
    # Now, delete it
    response = client.delete(f"/api/movies/{movie_id}")
    assert response.status_code == 200
    # Optionally, check it's gone
    response = client.get("/api/movies")
    movies = response.json()
    assert not any(m["id"] == movie_id for m in movies)

def test_api_add_movie_missing_fields():
    # Missing required field 'title'
    response = client.post("/api/movies", json={
        "director": "No Title",
        "year": 2022,
        "watched": False
    })
    assert response.status_code in (400, 422)  # FastAPI returns 422 for validation errors

def test_api_update_nonexistent_movie():
    response = client.put("/api/movies/99999", json={
        "title": "Ghost",
        "director": "Nobody",
        "year": 1900,
        "watched": False
    })
    assert response.status_code == 404

def test_api_delete_nonexistent_movie():
    response = client.delete("/api/movies/99999")
    assert response.status_code == 404

def test_search_movie_api():
    # This will call the real OMDb API if your key is set
    response = client.get("/search-movie?title=Inception")
    assert response.status_code == 200
    data = response.json()
    # It may return either movie data or an error, so check for both
    assert "title" in data or "error" in data

def test_ai_assistant_api():
    # This will call the real Groq API if your key is set
    payload = {
        "movie": {"title": "Inception", "director": "Nolan", "year": 2010, "watched": True},
        "question": "What is this movie about?"
    }
    response = client.post("/ai-assistant", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data