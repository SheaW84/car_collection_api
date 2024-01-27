from flask import Flask
from config import Config
from .site.routes import site
from .api.routes import api


app = Flask(__name__)