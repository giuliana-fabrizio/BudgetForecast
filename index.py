from flask import Flask, render_template
app = Flask(__name__)

from controllers.auth_controllers import *

app.secret_key = 'une clé (token) : grain de sel'
app.register_blueprint(auth_controllers)

@app.route('/')
def authentification():
    return render_template('authentification/base.html')