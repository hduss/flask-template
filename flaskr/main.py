from flask import Flask
from flask import request
from flask import render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/products")
def products():
    return "<p>Ici liste des produits</p>"


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    var = 'je suis une phrase'
    my_list = ['jean', 'david', 'emily']

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


@app.route('/<name>')
def error(name):
    render_template('error.html')


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        print('je suis ok')
    return render_template('admin/admin.html')


@app.route('/account/<id>')
def account(id=None):
    return render_template('headers/hello.html', id=id)
