import click

from flask.cli import with_appcontext
from werkzeug.security import check_password_hash, generate_password_hash


@click.command('init-admin')
@with_appcontext
def init_admin_user():
    """Clear the existing data and create new tables."""
    click.echo('Initialized an admin user')


def init_user(app, db):

    app.cli.add_command(init_admin_user)

