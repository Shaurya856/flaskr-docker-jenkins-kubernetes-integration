Flaskr
======

This project is based on the Flask `tutorial`_ application, modified to use PostgreSQL and SQLAlchemy instead of SQLite.

.. _tutorial: https://flask.palletsprojects.com/tutorial/

Installation
------------

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd flaskr-docker-jenkins-kubernetes-integration
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   # Or, if you are using the main branch, install Flask from source before installing Flaskr:
   # pip install -e ../..
   # pip install -e .
   ```

Environment Setup
----------------

1. Create a `.env` file in the project root:
   ```bash
   cp .env_template .env
   ```

2. Configure the following environment variables in `.env`:
   ```
   FLASK_APP=flaskr
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/postgres
   FLASK_DEBUG=1
   ```
   Note: If using Supabase, replace DATABASE_URL with your Supabase connection string.

Database Setup
--------------

1. Initialize the database:
   ```bash
   flask --app flaskr init-db
   ```
   This will create the necessary tables in your PostgreSQL database.

Running the Application
-----------------------

1. Start the Flask development server:
   ```bash
   flask --app flaskr run --debug
   ```

2. Open http://127.0.0.1:5000 in your browser.

Features
--------

- User registration and authentication (based on Flask tutorial)
- Create, read, update, and delete blog posts (based on Flask tutorial)
- User-specific post management (based on Flask tutorial)
- PostgreSQL database backend (modified from original SQLite implementation)
- SQLAlchemy ORM integration (modified from original SQLite implementation)
- Environment-based configuration

Testing
-------

Run the test suite:
```bash
pip install '.[test]'
pytest
```

For coverage report:
```bash
coverage run -m pytest
coverage report
coverage html  # open htmlcov/index.html in a browser
```

Development Notes
-----------------

This project maintains the core functionality of the Flask tutorial application while making the following modifications:

- Replaced SQLite with PostgreSQL for database backend
- Integrated SQLAlchemy ORM for database operations
- Added support for environment-based configuration
- Maintained the original blueprint-based application structure
- Kept the original authentication and blog post management features

Original Tutorial
-----------------

The original Flask tutorial can be found at:
https://flask.palletsprojects.com/tutorial/

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.
