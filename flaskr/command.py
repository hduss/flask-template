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
    click.echo(f'Password {password}!')
    generated_password = generate_password_hash(password)
    print(f'Password => {password}')

    db = get_db()
    request = 'INSERT INTO admin_user(email, password) VALUES(?, ?);'
    params = (email, generated_password)

    # print(db.execute(request, params).fetchone())
    try:
        db.execute(request, params).fetchone()
        db.commit()
    except sqlite3.Error as err:
        print(f'sqlite error: {err}')
        print(f'User {email} is already registered')





def init_user(app):

    # password = generate_password_hash()

    app.cli.add_command(init_admin_user)

