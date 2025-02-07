from flask import Blueprint, redirect, render_template, request, session, url_for
from queries.db_connexion import *
from queries.auth_queries import *

auth_controllers = Blueprint('auth_controllers', __name__, template_folder = 'templates')

@auth_controllers.teardown_app_request
def teardown_db(exception): close_db(exception)

@auth_controllers.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    customer = getUser(email, password)

    if customer:
        session.clear()
        session['id'] = customer['id']
        return "TODO : redirect(url_for('customer.controllers.home'))"

    return render_template('login.html')