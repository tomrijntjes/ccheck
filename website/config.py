#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

base_path = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
HOST = '0.0.0.0'
PORT = 80

SECRET_KEY = '\x15\xb6$R\xe4\xf2\x02l\x86\xd35\x7f\xb2\xad\xc9Mnla8\x9f\x0bnS'

UPLOAD_lAWYER_FOLDER = os.path.join(base_path, 'uploads_lawyer')
UPLOAD_COMPANY_FOLDER = os.path.join(base_path, 'uploads_company')

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

DATABASE_PATH = os.path.join(base_path, 'data')
if not os.path.exists(DATABASE_PATH):
    os.makedirs(DATABASE_PATH)
SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}/app.db'.format(DATABASE_PATH)
SQLALCHEMY_MIGRATE_REPO = '{0}/db_repository/'.format(DATABASE_PATH)

ADMINS = ['jensdebruijn@gmail.com']
