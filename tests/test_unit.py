import pytest
from unittest.mock import MagicMock, patch
from main import Movie

def test_movie_model_defaults():
    movie = Movie(title="Inception", director="Nolan", year=2010, watched=False)
    assert movie.title == "Inception"
    assert movie.director == "Nolan"
    assert movie.year == 2010
    assert movie.watched is False

# Example: Mocking the database session for adding a movie
@patch("main.SessionLocal")
def test_add_movie_logic(mock_session_local):
    # Arrange: Set up a fake session and movie
    mock_session = MagicMock()
    mock_session_local.return_value = mock_session
    from main import add_movie

    # Act: Call the function with test data
    response = add_movie(
        title="Interstellar",
        director="Nolan",
        year=2014,
        watched=True
    )

    # Assert: Check if the session methods were called
    assert mock_session.add.called
    assert mock_session.commit.called
    assert mock_session.refresh.called
    assert mock_session.close.called

# Example: Mocking OMDb API call in search_movie
@patch("main.requests.get")
def test_search_movie_found(mock_get):
    # Arrange: Set up a fake OMDb response
    mock_get.return_value.json.return_value = {
        "Response": "True",
        "Title": "Inception",
        "Director": "Christopher Nolan",
        "Year": "2010"
    }
    from main import search_movie

    # Act
    result = search_movie("Inception")

    # Assert
    assert result["title"] == "Inception"
    assert result["director"] == "Christopher Nolan"
    assert result["year"] == "2010"

@patch("main.requests.get")
def test_search_movie_not_found(mock_get):
    mock_get.return_value.json.return_value = {
        "Response": "False"
    }
    from main import search_movie
    result = search_movie("Nonexistent Movie")
    assert "error" in result

# Example: Mocking Groq API in ai_assistant
@patch("main.Groq")
def test_ai_assistant_success(mock_groq):
    # Arrange
    mock_client = MagicMock()
    mock_groq.return_value = mock_client
    mock_completion = MagicMock()
    mock_completion.choices = [MagicMock(message=MagicMock(content="Test answer"))]
    mock_client.chat.completions.create.return_value = mock_completion

    from main import ai_assistant

    payload = {
        "movie": {"title": "Inception", "director": "Nolan", "year": 2010, "watched": True},
        "question": "What is this movie about?"
    }
    result = ai_assistant(payload)
    assert "answer" in result
    assert result["answer"] == "Test answer"