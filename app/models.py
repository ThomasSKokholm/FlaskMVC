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
    

