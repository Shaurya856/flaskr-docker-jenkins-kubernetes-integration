from datetime import datetime
import os
from flask import current_app, g
import click
from . import db

def get_db():
    """Get the database session."""
    if 'db' not in g:
        g.db = db.session
    return g.db

def close_db(e=None):
    """Close the database connection."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """Initialize the database."""
    db.create_all()

@click.command('init-db')
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    """Register database functions with the Flask app."""
    # Register database functions
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

# Make the command available at module level
__all__ = ['get_db', 'init_db', 'init_db_command']
