# twitoff-ds15

## Installation

Download the repo, navigate there from the command line

## Setup
virtual enviornments

pipenv install
pipenv shell

## setup the database

# Windows users can omit the "FLASK_APP=web_app" part...

FLASK_APP=web_app flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the specified tables

## Usage

run the web app 

