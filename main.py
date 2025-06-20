# from fastapi import FastAPI, Request, Form, HTTPException
# from fastapi.responses import HTMLResponse, RedirectResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from sqlalchemy import create_engine, Column, Integer, String, Boolean
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import requests
# import os
# import json
# import requests as pyrequests
# from fastapi import Body
# from groq import Groq
# from dotenv import load_dotenv
# load_dotenv()


# # Database setup
# DATABASE_URL = "mysql+pymysql://movie_user:password123@localhost/movie_db"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# class Movie(Base):
#     __tablename__ = "movies"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(255), nullable=False)
#     director = Column(String(255))
#     year = Column(Integer)
#     watched = Column(Boolean, default=False)

# Base.metadata.create_all(bind=engine)

# # FastAPI setup
# app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")

# # OMDb API setup (replace with your own key)

# OMDB_API_KEY = os.environ.get("OMDB_API_KEY")

# # Home page
# @app.get("/", response_class=HTMLResponse)
# def read_root(request: Request):
#     db = SessionLocal()
#     movies = db.query(Movie).all()
#     db.close()
#     return templates.TemplateResponse("index.html", {"request": request, "movies": movies})

# # Search movie using OMDb API
# @app.get("/search-movie")
# def search_movie(title: str):
#     url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title}"
#     response = requests.get(url)
#     data = response.json()
#     if data.get("Response") == "True":
#         return {
#             "title": data.get("Title"),
#             "director": data.get("Director"),
#             "year": data.get("Year")
#         }
#     else:
#         return {"error": "Movie not found"}

# # Add a new movie
# @app.post("/movies")
# def add_movie(title: str = Form(...), director: str = Form(...), year: int = Form(...), watched: bool = Form(False)):
#     db = SessionLocal()
#     movie = Movie(title=title, director=director, year=year, watched=watched)
#     db.add(movie)
#     db.commit()
#     db.refresh(movie)
#     db.close()
#     return RedirectResponse("/", status_code=303)

# # Update a movie
# @app.post("/movies/{movie_id}/update")
# def update_movie(movie_id: int, title: str = Form(...), director: str = Form(...), year: int = Form(...), watched: bool = Form(False)):
#     db = SessionLocal()
#     movie = db.query(Movie).filter(Movie.id == movie_id).first()
#     if not movie:
#         db.close()
#         raise HTTPException(status_code=404, detail="Movie not found")
#     movie.title = title
#     movie.director = director
#     movie.year = year
#     movie.watched = watched
#     db.commit()
#     db.close()
#     return RedirectResponse("/", status_code=303)

# # Delete a movie
# @app.post("/movies/{movie_id}/delete")
# def delete_movie(movie_id: int):
#     db = SessionLocal()
#     movie = db.query(Movie).filter(Movie.id == movie_id).first()
#     if not movie:
#         db.close()
#         raise HTTPException(status_code=404, detail="Movie not found")
#     db.delete(movie)
#     db.commit()
#     db.close()
#     return RedirectResponse("/", status_code=303)

# # API endpoints for testing (CRUD)
# @app.get("/api/movies")
# def api_get_movies():
#     db = SessionLocal()
#     movies = db.query(Movie).all()
#     db.close()
#     return movies

# @app.post("/api/movies")
# def api_add_movie(movie: dict):
#     db = SessionLocal()
#     new_movie = Movie(**movie)
#     db.add(new_movie)
#     db.commit()
#     db.refresh(new_movie)
#     db.close()
#     return new_movie

# @app.put("/api/movies/{movie_id}")
# def api_update_movie(movie_id: int, movie: dict):
#     db = SessionLocal()
#     db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
#     if not db_movie:
#         db.close()
#         raise HTTPException(status_code=404, detail="Movie not found")
#     for key, value in movie.items():
#         setattr(db_movie, key, value)
#     db.commit()
#     db.close()
#     return {"message": "Movie updated"}

# @app.delete("/api/movies/{movie_id}")
# def api_delete_movie(movie_id: int):
#     db = SessionLocal()
#     db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
#     if not db_movie:
#         db.close()
#         raise HTTPException(status_code=404, detail="Movie not found")
#     db.delete(db_movie)
#     db.commit()
#     db.close()
#     return {"message": "Movie deleted"}



# @app.post("/ai-assistant")
# def ai_assistant(payload: dict = Body(...)):
#     movie = payload.get("movie", {})
#     question = payload.get("question", "")

#     prompt = (
#         f"You are a helpful movie assistant. The user is asking about the movie:\n"
#         f"Title: {movie.get('title', '')}\n"
#         f"Director: {movie.get('director', '')}\n"
#         f"Year: {movie.get('year', '')}\n"
#         f"Watched: {'Yes' if movie.get('watched', False) else 'No'}\n\n"
#         f"User's question: {question}\n"
#         f"Answer in not more than 30 words. Also try to answer in points (using -)"
#     )

#     try:
#         client = Groq(
#             api_key=os.environ.get("GROQ_API_KEY"),
#         )
#         chat_completion = client.chat.completions.create(
#             messages=[
#                 {
#                     "role": "user",
#                     "content": prompt,
#                 }
#             ],
#             model="llama3-70b-8192",
#             stream=False,
#         )
#         answer = chat_completion.choices[0].message.content.strip()
#     except Exception as e:
#         print("Groq API error:", e)  # <--- This will print the error in your terminal!
#         answer = "Sorry, I couldn't get an answer from the AI right now."

#     return {"answer": answer}









# Importing all the necessary libraries and modules for building the app
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
import os
import json
import requests as pyrequests
from fastapi import Body
from groq import Groq
from dotenv import load_dotenv

# Loading environment variables from the .env file (like API keys)
load_dotenv()

# Setting up the database connection and ORM
DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Defining the Movie model/table structure for storing movie data
class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    director = Column(String(255))
    year = Column(Integer)
    watched = Column(Boolean, default=False)

# Creating the movies table in the database if it doesn't exist
Base.metadata.create_all(bind=engine)

# Setting up the FastAPI app and configuring static files and templates
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Grabbing the OMDb API key from environment variables for movie search
OMDB_API_KEY = os.environ.get("OMDB_API_KEY")

# Handling the home page: showing the movie list using a template
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    db = SessionLocal()
    movies = db.query(Movie).all()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request, "movies": movies})

# Searching for a movie using the OMDb API and returning its details
@app.get("/search-movie")
def search_movie(title: str):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title}"
    response = requests.get(url)
    data = response.json()
    if data.get("Response") == "True":
        return {
            "title": data.get("Title"),
            "director": data.get("Director"),
            "year": data.get("Year")
        }
    else:
        return {"error": "Movie not found"}

# Adding a new movie to the database from the form submission
@app.post("/movies")
def add_movie(title: str = Form(...), director: str = Form(...), year: int = Form(...), watched: bool = Form(False)):
    db = SessionLocal()
    movie = Movie(title=title, director=director, year=year, watched=watched)
    db.add(movie)
    db.commit()
    db.refresh(movie)
    db.close()
    return RedirectResponse("/", status_code=303)

# Updating an existing movie's details in the database
@app.post("/movies/{movie_id}/update")
def update_movie(movie_id: int, title: str = Form(...), director: str = Form(...), year: int = Form(...), watched: bool = Form(False)):
    db = SessionLocal()
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        db.close()
        raise HTTPException(status_code=404, detail="Movie not found")
    movie.title = title
    movie.director = director
    movie.year = year
    movie.watched = watched
    db.commit()
    db.close()
    return RedirectResponse("/", status_code=303)

# Deleting a movie from the database
@app.post("/movies/{movie_id}/delete")
def delete_movie(movie_id: int):
    db = SessionLocal()
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        db.close()
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(movie)
    db.commit()
    db.close()
    return RedirectResponse("/", status_code=303)

# Providing API endpoints for CRUD operations (for API clients or testing)
@app.get("/api/movies")
def api_get_movies():
    db = SessionLocal()
    movies = db.query(Movie).all()
    db.close()
    return movies

@app.post("/api/movies")
def api_add_movie(movie: dict):
    db = SessionLocal()
    new_movie = Movie(**movie)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    db.close()
    return new_movie

@app.put("/api/movies/{movie_id}")
def api_update_movie(movie_id: int, movie: dict):
    db = SessionLocal()
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not db_movie:
        db.close()
        raise HTTPException(status_code=404, detail="Movie not found")
    for key, value in movie.items():
        setattr(db_movie, key, value)
    db.commit()
    db.close()
    return {"message": "Movie updated"}

@app.delete("/api/movies/{movie_id}")
def api_delete_movie(movie_id: int):
    db = SessionLocal()
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not db_movie:
        db.close()
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(db_movie)
    db.commit()
    db.close()
    return {"message": "Movie deleted"}

# Handling AI assistant requests: sending movie info and user question to Groq LLM and returning the answer
@app.post("/ai-assistant")
def ai_assistant(payload: dict = Body(...)):
    movie = payload.get("movie", {})
    question = payload.get("question", "")

    prompt = (
        f"You are a helpful movie assistant. The user is asking about the movie:\n"
        f"Title: {movie.get('title', '')}\n"
        f"Director: {movie.get('director', '')}\n"
        f"Year: {movie.get('year', '')}\n"
        f"Watched: {'Yes' if movie.get('watched', False) else 'No'}\n\n"
        f"User's question: {question}\n"
        f"Answer in not more than 30 words. Also try to answer in points (using -). Start writing the answer directly and no need to use any phrase like Here's the answer:"
    )

    try:
        # Creating a Groq client and sending the prompt to the LLM
        client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-70b-8192",
            stream=False,
        )
        answer = chat_completion.choices[0].message.content.strip()
    except Exception as e:
        # Logging any errors and returning a fallback message
        print("Groq API error:", e)
        answer = "Sorry, I couldn't get an answer from the AI right now."

    return {"answer": answer}