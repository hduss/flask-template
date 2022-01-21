# Initialisation
    
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
    create SQL skeleton in sql/schema.sql
    flask init-db