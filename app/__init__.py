#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
<<<<<<< Updated upstream
from flask_bootstrap import Bootstrap
=======
from flask_login import LoginManager
>>>>>>> Stashed changes

from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()

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

    login_manager.init_app(app)
    login_manager.login_message = "Login, before accessing this page."
    login_manager.login_view = "auth.login"

    return app
