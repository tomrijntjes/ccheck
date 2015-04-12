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
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(54))
    template1 = db.Column(db.String(300))
    template2 = db.Column(db.String(300))
    template3 = db.Column(db.String(300))
    auto = db.Column(db.String(3))
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
        self.auto = "on"
        self.template1 = '''
        <p>Beste __KLANT__,</p>
        <p>u heeft een contract geupload bij onze contractservice. Door __VERANDERING WET__&nbsp;heeft dat contract __NAAM CONTRACT__&nbsp;uw aandacht nodig: __AANDACHTSPUNT__. Als u daarvoor onze hulp kunt gebruiken horen we dat graag.</p>
        <p>Met hartelijke groet,</p>
        <p>__UW NAAM__</p>
        '''
        self.template2 = '''
        <p>Beste __KLANT__,</p>
        <p>u heeft een contract geupload bij onze contractservice. Door __VERANDERING WET__&nbsp;heeft dat contract __NAAM CONTRACT__&nbsp;uw aandacht nodig: __AANDACHTSPUNT__. Als u daarvoor onze hulp kunt gebruiken horen we dat graag.</p>
        <p>Met hartelijke groet,</p>
        <p>__UW NAAM__</p>
        '''
        self.template3 = '''
        <p>Beste __KLANT__,</p>
        <p>we hebben uw contract __NAAM CONTRACT__ geregistreerd en gecontroleerd. Alles is in orde! Wij zorgen ervoor dat als uw contract een update nodig heeft, u meteen een bericht ontvangt. Dat scheelt eventuele nare verrassingen.</p>
        <p>Met hartelijke groet,</p>
        <p>__UW NAAM__</p>
        '''

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
