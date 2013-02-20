# -*- coding: utf-8 -*-
"""
    DataView
    ~~~~~~


    :author: Thejesh GN.
    :license: BSD, see LICENSE for more details.
"""

from __future__ import with_statement
import os
from sqlite3 import dbapi2 as sqlite3
from jinja2 import Environment, FileSystemLoader
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack
from flask import Module, make_response, render_template

# configuration
DEBUG = True
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)
try:
    app.config.from_object('settings')
except ImportError:
    import sys
    print >> sys.stderr, "Please create a settings.py with the necessary settings."
    print >> sys.stderr, "You may use the site without these settings, but some features may not work."

jinja_env = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
    return top.sqlite_db

@app.before_request
def before_request():
    method = request.form.get('_method', '').upper()
    if method:
        request.environ['REQUEST_METHOD'] = method
        ctx = flask._request_ctx_stack.top
        ctx.url_adapter.default_method = method
        assert request.method == method

@app.teardown_appcontext
def close_db_connection(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()


@app.route('/')
def home():
    db = get_db()
    template = jinja_env.get_template('home.html')
    return template.render()

@app.route('/formsList',methods=['HEAD','POST','GET'])
def formsList():



@app.route('/submission',methods=['HEAD','POST'])
def submission():
    if request.environ['REQUEST_METHOD'] == 'HEAD':
        response = make_response(render_template('head_request.txt'))
        response.headers['X-OpenRosa-Version'] = '1'
        return response, 204
    elif request.environ['REQUEST_METHOD'] == 'POST':
        response = make_response(render_template('home.html'))
        response.headers['X-OpenRosa-Version'] = '1'
        return response, 201




if __name__ == '__main__':
    app.run()