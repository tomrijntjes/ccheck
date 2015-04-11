#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.uploads import UploadSet, DOCUMENTS

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

login_manager = LoginManager()
from .models import Anonymous
login_manager.anonymous_user = Anonymous
login_manager.init_app(app)

documents = UploadSet('documents', DOCUMENTS)

from app import index, user, forms, user, contracten
