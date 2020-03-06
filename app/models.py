#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class Humanbeing(UserMixin, db.Model):
    """Create an Human being table"""
    __tablename__ = 'humanbeings'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), index=True, unique=True)
    callname = db.Column(db.String(255), index=True, unique=True)
    first_name = db.Column(db.String(255), index=True)
    last_name = db.Column(db.String(255), index=True)
    password_hash = db.Column(db.String(128))
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    is_admin =  db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """Password acces prevention."""
        raise AttributeError('Password is not readable, for safy reason.')

    @password.setter
    def password(self, password):
        """Make the password hashed"""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """Check if hashed password is correct"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Human being: {}>'.format(self.callname)

@login_manager.user_loader
def load_user(user_id):
    return Humanbeing.query.get(int(user_id))


class Address(db.Model):
    """Table for adresses"""
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    road = db.Column(db.String(255), unique=True)
    postalcode = db.Column(db.Integer)
    contry = db.Column(db.String(255))
    Humanbeing = db.relationship('Humanbeing', backref='adress', lazy='dynamic')

    def __repr__(self):
        return '<Adress: {}>'.format(self.road)

    

