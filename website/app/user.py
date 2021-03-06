#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import url_for, redirect, flash, session, request, render_template
from flask.ext.login import login_required, login_user, logout_user, current_user
from .forms import SignupForm, LoginForm
from app import app, db, login_manager

from .functions import flash_errors, admin_required

from .models import User

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route('/instellingen', methods=['GET', 'POST'])
@admin_required
@login_required
def instellingen():
    all_q = User.query.all()
    all = []
    for one in all_q:
        all.append(one.name)
    customer_query = current_user.followed.all()
    customers = []
    for customer_q in customer_query:
        customers.append(customer_q.name)
    pot_customers = [x for x in all if x not in customers]
    pot_customers.remove(current_user.name)
    template1 = current_user.template1
    template2 = current_user.template2
    template3 = current_user.template3

    if request.method == 'POST':
        auto = request.form.getlist('auto')[0]
        current_user.auto = auto
        template1 = request.form.getlist('edit1')[0]
        template2 = request.form.getlist('edit2')[0]
        template3 = request.form.getlist('edit3')[0]
        current_user.template1 = template1
        current_user.template2 = template2
        current_user.template3 = template3
        db.session.add(current_user)
        db.session.commit()

    return render_template('instellingen.html', template1=template1, template2=template2, template3=template3, customers=customers, pot_customers=pot_customers)

@app.route('/add_customer/<name>')
@admin_required
@login_required
def add_customer(name):
    name = name.title()
    user = User.query.filter_by(name=name).first()
    if user is None:
        flash('User %s not found.' % name, )
        return redirect(url_for('instellingen'))
    if user == current_user:
        return redirect(url_for('instellingen'))
    u = current_user.follow(user)
    if u is None:
        return redirect(url_for('instellingen'))
    db.session.add(u)
    db.session.commit()
    return redirect(url_for('instellingen'))

@app.route('/remove_customer/<name>')
@admin_required
@login_required
def unfollow(name):
    name = name.title()
    user = User.query.filter_by(name=name).first()
    if user is None:
        return redirect(url_for('instellingen'))
    if user == current_user:
        return redirect(url_for('instellingen'))
    u = current_user.unfollow(user)
    if u is None:
        return redirect(url_for('instellingen'))
    db.session.add(u)
    db.session.commit()
    return redirect(url_for('instellingen'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if current_user.is_authenticated():
      flash('You are already logged in', 'info')
      return redirect(url_for('index'))
  form = SignupForm()
  if request.method == 'POST':
    if form.validate() == False:
        flash_errors(form)
        return render_template('signup.html', form=form)
    else:
      user = User(form.name.data, form.email.data, form.password.data)
      db.session.add(user)
      db.session.commit()
      login_user(user, remember=True)
      return redirect(url_for('index'))
  elif request.method == 'GET':
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        flash('You are already logged in', 'info')
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash_errors(form)
            return render_template('login.html', form=form)
        else:
            email = form.email.data
            user = User.query.filter_by(email=email).first()
            login_user(user, remember=True)
            flash('Logged in succesfully', 'success')
            return redirect(url_for('index'))
    elif request.method == 'GET':
        return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out succesfully','success')
    return redirect(url_for('index'))

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))
