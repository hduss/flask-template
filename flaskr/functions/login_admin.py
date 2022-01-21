from flask import flash


def login(request):
    valid_email = 'delmas.theo.dev@gmail.com'
    valid_password = 'root'

    print(request.form['email'])
    email = request.form['email']
    password = request.form['password']

    if email == valid_email and password == valid_password:
        return True

    return False
