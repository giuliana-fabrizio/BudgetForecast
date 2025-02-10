from flask import Blueprint, flash, session, redirect, render_template, request, url_for
from datetime import datetime
from queries.db_connexion import *
from queries.categories_queries import *

category_controllers = Blueprint('category_controllers', __name__, template_folder = 'templates')

@category_controllers.teardown_app_request
def teardown_db(exception): close_db(exception)

@category_controllers.route('/categories')
def displayCategories():
    categories = getCategories()
    return render_template('/categories/list.html', length=len(categories), categories=categories)

@category_controllers.route('/category/add', methods=['GET', 'POST'])
def addCategory():
    if request.method == 'GET':
        return render_template(
            '/categories/form.html',
            action="/category/add",
            title="Ajouter une catégorie"
        )

    name = request.form['name']
    forecast = request.form['forecast']
    created_at = datetime.now()
    id_customer = session['id']

    insertCategory(name, forecast, created_at, created_at, id_customer)

    flash('Information: catégorie ajoutée avec succès', 'success')
    return redirect(url_for('category_controllers.displayCategories'))

@category_controllers.route('/category/edit/<id>', methods=['GET', 'POST'])
def editCategory(id):
    if request.method == 'GET':
        category = getCategory(id)
        if not category:
            flash('Erreur: catégorie inexistante', 'danger')
            return redirect(url_for('category_controllers.displayCategories'))

        return render_template(
            '/categories/form.html',

            action="/category/edit/" + id,
            title="Modifier une catégorie",

            name=category['name'],
            forecast=category['forecast']
        )

    name = request.form['name']
    forecast = request.form['forecast']
    updated_at = datetime.now()

    updateCategory(name, forecast, updated_at, id)

    flash('Information: catégorie modifiée avec succès', 'success')
    return redirect(url_for('category_controllers.displayCategories'))

@category_controllers.route('/category/remove/<id>', methods=['GET', 'POST'])
def removeCategory(id):
    category = getCategory(id)
    if not category:
        flash('Erreur: catégorie inexistante', 'danger')
        return redirect(url_for('category_controllers.displayCategories'))

    deleteCategory(id)

    flash('Information: catégorie supprimée avec succès', 'success')
    return redirect(url_for('category_controllers.displayCategories'))