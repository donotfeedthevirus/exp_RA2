from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint('auth', __name__, template_folder='templates')

users = {
    "user1": "1234",
    "user2": "1234"
}

@auth_bp.route('/')
def login():
    return render_template('login.html')

@auth_bp.route('/validated_user', methods=['POST'])
def validated_user():
    user     = request.form['user']
    password = request.form['password']
    if users.get(user) == password:
        return redirect(url_for('dashboard.home'))
    return '<h1>Credenciais Invalidas!</h1>', 401

@auth_bp.route('/users')
def list_users():
    return render_template('users.html', users=users)

@auth_bp.route('/users/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        user = request.form['user']
        pwd  = request.form['password']
        users[user] = pwd
        return redirect(url_for('auth.list_users'))
    return render_template('register_user.html')

@auth_bp.route('/users/delete', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        user = request.form['user']
        users.pop(user, None)
        return redirect(url_for('auth.list_users'))
    return render_template('remove_user.html', users=users)
