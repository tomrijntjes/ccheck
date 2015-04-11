#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app import app, db
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.login import AnonymousUserMixin

followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(54))
    template1 = db.Column(db.String(300))
    template2 = db.Column(db.String(300))
    template3 = db.Column(db.String(300))
    followed = db.relationship('User',
                               secondary=followers,
                               primaryjoin=(followers.c.follower_id == id),
                               secondaryjoin=(followers.c.followed_id == id),
                               backref=db.backref('followers', lazy='dynamic'),
                               lazy='dynamic')

    def __init__(self, name, email, password):
        self.name = name.title()
        self.email = email.lower()
        self.set_password(password)
        self.template1 = 'This is a test <<hello>>'
        self.template2 = 'This is a test <<goedemorgen>>'
        self.template3 = 'This is a test <<ja daaaag>>'

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            return self

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            return self

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    def is_admin(self):
        return self.email in app.config['ADMINS']

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_anonymous(self):
        return False

class Anonymous(AnonymousUserMixin):
  def __init__(self):
    self.username = 'Guest'

  def is_admin(self):
    return False
