from flask import Flask
import json
import urllib3
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

from application import routes
