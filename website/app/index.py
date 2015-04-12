#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prototype')
def test():
    return render_template('prototype.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
