import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('/', __name__, url_prefix='/')


@bp.route('/')
def index():
    print('je suis blueprint front')
    return render_template('index.html')


@bp.route("/services")
def services():
    return render_template(url_for())


@bp.route("/contact", methods=['GET', 'POST'])
def contact():
    print('contact blueprint')
    contact_select = {
        'probleme': 'problème sur le site',
        'rendez-vous': 'Je souhaite prendre rendez-vous',
    }

    if request.method == 'POST':
        print(request.values)

    return render_template('contact.html', contact_select=contact_select)


@bp.route('/find')
def find():
    return render_template('front/find.html')


@bp.route('/<not_founded>')
def error(not_founded):
    print(f'Error page => {not_founded}')
    return render_template('404.html')

# @bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return "<p>Page login ici</p>"
#         # return show_the_login_form()
