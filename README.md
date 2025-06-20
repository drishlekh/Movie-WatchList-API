Movie WatchList API
===================

A modern web application for managing your personal movie watchlist. Add, update, search, and delete movies, and get instant answers to your movie questions with an integrated AI assistant.

Features
--------

*   **Full CRUD API:** Create, read, update, and delete movies in your watchlist.
    
*   **MySQL Database Integration:** Securely store and manage your movie data.
    
*   **Movie Search:** Instantly fetch movie details from the OMDb API.
    
*   **Modern Frontend:** Sleek, glassy UI for a great user experience.
    
*   **AI Assistant:** Ask questions about any movie in your list and get smart, concise answers powered by Groq LLM.
    
*   **API Docs:** Explore and test your API at /docs.
    

Installation
------------

1.  git clone https://github.com/drishlekh/Movie-WatchList-API.git cd Movie-WatchList-API
    
2.  python -m venv venv
    
    *   On Windows: venv\\Scripts\\activate
        
    *   On Mac/Linux: source venv/bin/activate
        
3.  pip install -r requirements.txt
    
4.  Create a .env file in the project root with the following content:
DATABASE\_URL=mysql+pymysql://movie\_user:<password123>@localhost/movie\_db 
OMDB\_API\_KEY=your\_omdb\_api\_key 
GROQ\_API\_KEY=your\_groq\_api\_key 
{Replace the values with your actual credentials}
    
5.  **Set up the database:**
    
    *   Make sure you have a MySQL server running and a database named movie\_db created.
        
    *   Update the DATABASE\_URL in your .env file if your credentials are different.
        

Running the App
---------------

Start the FastAPI server with:


* uvicorn main:app --reload
* Visit http://localhost:8000 in your browser to use the app.
* Access the interactive API docs at http://localhost:8000/docs or use Postman.
    

API Overview
------------
Uploaded as API_Documentation.txt in project folder


MySQL Commands
---------------

Open your MySQL command line or MySQL Workbench and log in as the root user (or any admin user).

*   Create a new database called movie\_db by running:CREATE DATABASE movie\_db;
    
*   Create a new user named movie\_user with the password password123 by running:CREATE USER 'movie\_user'@'localhost' IDENTIFIED BY 'password123';
    
*   Give this user all privileges on the movie\_db database by running:GRANT ALL PRIVILEGES ON movie\_db.\* TO 'movie\_user'@'localhost';
    
*   Apply the changes by running:FLUSH PRIVILEGES;
    
*   You can now exit the MySQL prompt by typing:EXIT;
