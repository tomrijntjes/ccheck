#!/usr/bin/python3
# -*- coding: utf-8 -*-

from migrate.versioning import api
from app import db
import os.path

from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO

class Database:
    def __init__(self):
        if not os.path.isfile(SQLALCHEMY_DATABASE_URI.replace('sqlite:///', '')):
            db.create_all()
            if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
                api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
                api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
            else:
                api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

Database()
