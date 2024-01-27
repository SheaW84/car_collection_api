from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from flask_login import UserMixin
from flask_login import LoginManager

login_manager = LoginManager()
db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable=True, default='')
    last_name = db.Column(db.String(150), nullable=True, default='')
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String, nullable=True, default='')
    token = db.Column(db.String, default='', unique = True)
    date_created = db.Column(db.Datetime, nullable = False, default = datetime.utcnow)
