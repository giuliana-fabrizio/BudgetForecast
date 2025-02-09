from flask import Flask, render_template

from controllers.auth_controllers import *
from controllers.revenue_controllers import *

app = Flask(__name__)
app.secret_key = 'une clé (token) : grain de sel'

app.register_blueprint(auth_controllers)
app.register_blueprint(revenue_controllers)

@app.route('/')
def authentification():
    return render_template('login.html')