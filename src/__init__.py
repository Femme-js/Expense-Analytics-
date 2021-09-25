"""This is init module."""
from flask_restful import Api
from flask import Flask
import os
from src.routes import initialize_routes
#from config import Config
# Place where app is defined
app = Flask(__name__)
#app.config.from_object(Config)
api = Api(app)

initialize_routes(api)
