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
    return render_template('/revenues/list.html', length=len(revenues), revenues=revenues)

@revenue_controllers.route('/revenue/add', methods=['GET', 'POST'])
def addRevenue():
    if request.method == 'GET':
        return render_template(
            '/revenues/form.html',
            action="/revenue/add",
            title="Ajouter un revenu"
        )

    name = request.form['name']
    amount = request.form['amount']
    created_at = datetime.now()
    id_customer = session['id']

    insertRevenue(name, amount, created_at, created_at, id_customer)

    flash('Information: revenu ajouté avec succès', 'success')
    return redirect(url_for('revenue_controllers.displayRevenues'))

@revenue_controllers.route('/revenue/edit/<id>', methods=['GET', 'POST'])
def editRevenue(id):
    if request.method == 'GET':
        revenue = getRevenue(id)
        if not revenue:
            flash('Erreur: revenu inexistant', 'danger')
            return redirect(url_for('revenue_controllers.displayRevenues'))
        return render_template(
            '/revenues/form.html',

            action="/revenue/edit/" + id,
            title="Modifier un revenu",

            name=revenue['name'],
            amount=revenue['amount']
        )

    name = request.form['name']
    amount = request.form['amount']
    updated_at = datetime.now()

    updateRevenue(name, amount, updated_at, id)

    flash('Information: revenu modifié avec succès', 'success')
    return redirect(url_for('revenue_controllers.displayRevenues'))

@revenue_controllers.route('/revenue/remove/<id>', methods=['GET', 'POST'])
def removeRevenue(id):
    revenue = getRevenue(id)
    if not revenue:
        flash('Erreur: revenu inexistant', 'danger')
        return redirect(url_for('revenue_controllers.displayRevenues'))

    deleteRevenue(id)

    flash('Information: revenu supprimé avec succès', 'success')
    return redirect(url_for('revenue_controllers.displayRevenues'))