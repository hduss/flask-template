from flask import Flask
from flask import request
from flask import render_template
from flask_admin import Admin
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route("/products")
def products():
    return "<p>Ici liste des produits</p>"

@app.route("/contact")
def contact():
    return render_template()
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return "<p>Page login ici</p>"
        # return show_the_login_form()

@app.route('/account/<id>')
def account(id=None):
    return render_template('headers/hello.html', id=id)

def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"