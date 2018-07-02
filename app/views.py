# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session, request
from app import application

application.jinja_env.add_extension('jinja2.ext.do')
#-----------------      STATUS  -----------------

@application.route('/status')
def route_status():
        return 'ONLINE'

@application.route('/server_name')
def route_server_name():
        return 'Pyche Sample'

#-----------------      STATUS  -----------------

#-----------------      PAGES   -----------------

@application.route('/')
def route_index():
        return render_template('index.html')

#-----------------      PAGES   -----------------