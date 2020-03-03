#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv

from app import create_app

load_dotenv()

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    if app.config['DEBUG'] == True:
        app.run(host='0.0.0.0', debug=True, port='5063')
    else:
        app.run(host='0.0.0.0', debug=False, port='5063')
