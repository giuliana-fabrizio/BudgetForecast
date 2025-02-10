from flask import Blueprint, flash, session, redirect, render_template, request, url_for
from datetime import datetime
from queries.db_connexion import *
from queries.revenues_queries import *

revenue_controllers = Blueprint('revenue_controllers', __name__, template_folder = 'templates')

@revenue_controllers.teardown_app_request
def teardown_db(exception): close_db(exception)

@revenue_controllers.route('/revenues')
def displayRevenues():
    revenues = getRevenues()
    return render_template('/revenues/list.html', revenues=revenues)

@revenue_controllers.route('/revenue/add', methods=['GET', 'POST'])
def addRevenue():
    if request.method == 'GET':
        return render_template('/revenues/form.html', title="Ajouter un revenu")

    name = request.form['name']
    amount = request.form['amount']
    created_at = datetime.now()
    id_customer = session['id']

    insertRevenue(name, amount, created_at, created_at, id_customer)

    flash('Information: revenu ajouté avec succès', 'success')
    return redirect(url_for('revenue_controllers.displayRevenues'))