from flask import Blueprint, render_template
from queries.db_connexion import *
from queries.revenues_queries import *

revenue_controllers = Blueprint('revenue_controllers', __name__, template_folder = 'templates')

@revenue_controllers.teardown_app_request
def teardown_db(exception): close_db(exception)

@revenue_controllers.route('/revenues')
def displayRevenues():
    revenues = getRevenues()
    return render_template('/revenues/list.html', revenues=revenues)