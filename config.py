#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Config(object):
    """base config class"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    """Dev configs"""
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////sqlite_dev_db.db'


class ProdConfig(Config):
    """For production"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////sqlite_db.db'

app_config = {
    'dev': DevConfig,
    'prod': ProdConfig
}