#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from config import app_config
from app import views

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True, static_url_path='/static')
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../config.py')
    db.init_app(app)
    bootstrap = Bootstrap(app)

    @app.route('/404')
    def NoFound404():
        return render_template("404.html")

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/about')
    def about():
        return render_template("about.html")

    return app
