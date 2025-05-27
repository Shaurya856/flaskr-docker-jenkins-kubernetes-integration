import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    
    # Configure the app
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY=os.getenv('SECRET_KEY', 'dev'),
        # Configure PostgreSQL
        SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/postgres'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize SQLAlchemy
    db.init_app(app)

    # register the database commands
    from .db import init_db_command
    app.cli.add_command(init_db_command)

    # apply the blueprints to the app
    from . import auth
    from . import blog

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    app.add_url_rule("/", endpoint="index")

    return app
