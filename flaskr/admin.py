import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/', methods=['GET', 'POST'])
def index():
    error = None
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('admin.login'))

    if request.method == 'POST':
        # functions.login_admin(request)
        # return login_admin.login(request)

        valid_email = 'delmas.theo.dev@gmail.com'
        valid_password = 'root'

        print(request.form['email'])
        email = request.form['email']
        password = request.form['password']

        if email == valid_email and password == valid_password:

            flash('Mauvais identifiants')
        else:
            flash('Mauvais identifiants', 'error')
            error = 'Mauvais identifiants'
            # return render_template('admin/admin.html', error=error)

    return render_template('admin/admin.html', error=error)


@bp.route('login')
def login():

    user_id = session.get('user_id')
    # if user_id is None:
       # return redirect(url_for('admin.index'))
    return render_template('admin/login.html')


@bp.before_app_request
def load_logged_in_user():
    print('je suis avant chaque route')
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
        # return redirect(url_for('admin.login'))
        # return redirect(url_for('admin.index'))
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

        print(g.user)
