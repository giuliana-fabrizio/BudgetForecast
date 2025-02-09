from flask import Blueprint, flash, request, render_template
from queries.db_connexion import *
from queries.customer_queries import *

customer_controllers = Blueprint('customer_controllers', __name__, template_folder = 'templates')

@customer_controllers.teardown_app_request
def teardown_db(exception): close_db(exception)

def checkPassword(password, password_verified):
    if password != password_verified: return 'Attention: les mots de passe doivent être identiques'
    if len(password) < 10: return 'Attention: le mot de passe doit comporter 10 caractères minimum'
    return None

@customer_controllers.route('/create-an-account', methods=['GET', 'POST'])
def create_an_account():
    args = {'action': 'signup', 'title': 'Création de compte'}

    if request.method == 'GET': return render_template('/authentification/base.html', **args)

    email = request.form['email']
    if getUserByEmail(email):
        flash('Erreur : le mail saisi est déjà utilisé', 'danger')
        return render_template('/authentification/base.html', **args)

    password, password_verified = request.form['password'], request.form['password_verified']
    isGoodPassword = checkPassword(password, password_verified)
    if isGoodPassword:
        flash(isGoodPassword, 'warning')
        return render_template('/authentification/base.html', **args)

    firstname, name = request.form['firstname'], request.form['name']
    addUser(firstname, name, email, password)

    flash('Information : compte créé avec succès', 'success')
    return render_template('/authentification/base.html', action='signin')