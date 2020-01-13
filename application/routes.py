from flask import render_template
from flask import send_from_directory
from application import app
import os

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Logan'}
    return render_template('index.html', title = 'Home', user = user)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

