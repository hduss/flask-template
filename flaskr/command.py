import sqlite3

import click

from flask.cli import with_appcontext
from werkzeug.security import check_password_hash, generate_password_hash
from .db import get_db


@click.command('init-admin')
@click.argument('email')
@click.argument('password')
@with_appcontext
def init_admin_user(email, password):
    click.echo(f'Email: {email}')
    click.echo(f'Password: {password}!')

    insert = None
    generated_password = generate_password_hash(password)
    db = get_db()

    request = 'INSERT INTO admin_user(email, password) VALUES(?, ?);'
    params = (email, generated_password)

    try:
        insert = db.execute(request, params).fetchone()
        db.commit()
        print(f'User {email} added')

    except sqlite3.Error as err:
        print(f'\nsqlite error: {err}')
        print(f'User {email} is already registered')

    db.close()


def init_user(app):

    app.cli.add_command(init_admin_user)
