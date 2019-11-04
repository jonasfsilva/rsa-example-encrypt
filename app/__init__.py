
# app/__init__.py
from flask import Flask
from .views import blueprint as api_encrypt


app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(api_encrypt)
# app.register_blueprint(api_dencrypt)

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py', silent=True)

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE', silent=True)