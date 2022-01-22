# Initialization
    
## On linux
    export FLASK_APP=flaskr
    export FLASK_ENV=development (DEBUG)
    flask run
        * Running on http://127.0.0.1:5000/
## On windows
    set FLASK_APP=flaskr
    set FLASK_ENV=development (DEBUG) 
    flask run
        * Running on http://127.0.0.1:5000/

## Init database
    Create SQL skeleton in sql/schema.sql
    NEED : 
    CREATE TABLE admin_user (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      email TEXT UNIQUE NOT NULL,
      password TEXT NOT NULL
    );

    flask init-db

# Use
## Create an administration user
    flask init-admin email password

    