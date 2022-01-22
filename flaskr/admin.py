from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def index():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('admin.login'))

    return render_template('admin/admin.html')


@bp.route('login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        db = get_db()
        user = db.execute(
            'SELECT * FROM admin_user WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('admin.index'))

    return render_template('admin/login.html', error=error)


@bp.route('logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return render_template('admin/login.html')


@bp.before_app_request
def load_logged_in_user():
    print('je suis avant chaque route')
    user_id = session.get('user_id')
    print(f'User session id: {user_id}')

    if user_id is None:
        g.user = None
        # return redirect(url_for('admin.login'))
        # return redirect(url_for('admin.index'))
    else:
        print(f'User connected')
        # g.user = get_db().execute(
        #     'SELECT * FROM user WHERE id = ?', (user_id,)
        # ).fetchone()
        #
        # print(g.user)
