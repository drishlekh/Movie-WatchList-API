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

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`uvicorn main:app --reload`  

*   Visit [http://localhost:8000](http://localhost:8000) in your browser to use the app.
    
*   Access the interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs) or use Postman.
    

API Overview
------------

*   **Get All Movies:**GET /api/moviesRetrieve all movies in the watchlist.
    
*   **Add a New Movie:**POST /api/moviesAdd a new movie to the watchlist.Request body: title, director, year, watched.
    
*   **Update a Movie:**PUT /api/movies/{movie\_id}Update details of an existing movie.Request body: title, director, year, watched.
    
*   **Delete a Movie:**DELETE /api/movies/{movie\_id}Delete a movie from the watchlist.
    
*   **Search for a Movie (OMDb):**GET /search-movie?title=MovieTitleSearch for a movie by title using the OMDb API.
    
*   **AI Assistant:**POST /ai-assistantAsk a question about a movie and get an AI-generated answer.Request body: movie (object), question (string).
