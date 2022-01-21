import flaskr.functions.login_admin as login_admin

from flask import Flask
from flask import request
from flask import render_template
from flask import flash
from flask import session
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/products")
def products():
    return "<p>Ici liste des produits</p>"


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    contact_select = {
        'probleme': 'problème sur le site',
        'rendez-vous': 'Je souhaite prendre rendez-vous',
    }

    if request.method == 'POST':
        print(request.values)

    return render_template('contact.html', contact_select=contact_select)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return "<p>Page login ici</p>"
        # return show_the_login_form()


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    error = None
    if request.method == 'POST':
        # functions.login_admin(request)
        # return login_admin.login(request)

        if login_admin.login(request):
            flash('Mauvais identifiants')
        else:
            flash('Mauvais identifiants', 'error')
            error = 'Mauvais identifiants'
            # return render_template('admin/admin.html', error=error)

    return render_template('admin/admin.html', error=error)


@app.route('/admin/')

# @app.route('/<name>')
# def error(name):
#     render_template('error.html')
#


@app.route('/account/<id>')
def account(id=None):
    return render_template('headers/hello.html', id=id)
