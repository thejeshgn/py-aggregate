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
from flask import Response
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

@app.route('/formList',methods=['HEAD','POST','GET'])
def formList():
    xml = """<?xml version='1.0' encoding='UTF-8' ?>
<xforms xmlns="http://openrosa.org/xforms/xformsList">
  <xform>
    <formID>mydomain.org:formId</formID>
    <name>Form with zero or more additional files</name>
    <version>1.1</version>
    <hash>md5:c28fc778a9291672badee04ac880a05d</hash>
    <descriptionText>A possibly very long description of the form</descriptionText>
    <downloadUrl>http://myhost.com/app/path/getMe/formIdA</downloadUrl>
  </xform>
  <xform>
    <formID>http://mydomain.org/uniqueFormXmlns</formID>
    <name>Form without additional files</name>
    <version>v50 alpha</version>
    <hash>md5:c28fc778a9291672badee04ac770a05d</hash>
    <descriptionUrl>http://mysecondhost.com/a/description/getMe@formId=uniqueKey</descriptionUrl>
    <downloadUrl>http://mysecondhost.com/a/different/path/getMe@formId=uniqueKey</downloadUrl>
  </xform>
  <xforms-group>
     <groupID>someId</groupID>
     <name>Short name of grouping</name>
     <listUrl>http://whateverhost.com/other/path/forDownload?group=fido</listUrl>
     <descriptionText>Longer description of what is here</descriptionText>
     <descriptionUrl>http://morehost.com/description/link</descriptionUrl>
  </xforms-group>
</xforms>"""
    print xml
    response = Response(xml, mimetype='text/xml')
    response.headers['X-OpenRosa-Version'] = '1'
    return response

@app.route('/getForm',methods=['HEAD','POST','GET'])
def getForm():
    xml ="""
<h:html xmlns="http://www.w3.org/2002/xforms" xmlns:h="http://www.w3.org/1999/xhtml" xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:jr="http://openrosa.org/javarosa">
  <h:head>
    <h:title>Customer Billing</h:title>
    <model>
      <instance>
        <data id="Customer_Billing_Addition_123">
          <meta>
            <instanceID/>
          </meta>
          <customer_mobile/>
          <bill_amount/>
          <billing_period_start_date/>
          <billing_period_end_date/>
        </data>
      </instance>
      <itext>
        <translation lang="eng">
          <text id="/data/customer_mobile:label">
            <value>Customer Mobile</value>
          </text>
          <text id="/data/customer_mobile:hint">
            <value>Existing Customer Mobile Number</value>
          </text>
          <text id="/data/customer_mobile:constraintMsg">
            <value>Customer Mobile</value>
          </text>
          <text id="/data/bill_amount:label">
            <value>Bill Amount</value>
          </text>
          <text id="/data/billing_period_start_date:label">
            <value>Billing Period Start Date</value>
          </text>
          <text id="/data/billing_period_end_date:label">
            <value>Billing Period End Date</value>
          </text>
        </translation>
      </itext>
      <bind nodeset="/data/meta/instanceID" type="string" readonly="true()" calculate="concat('uuid:', uuid())"/>
      <bind nodeset="/data/customer_mobile" type="long" required="true()" />
      <bind nodeset="/data/bill_amount" type="int" required="true()" constraint="(. &gt;= '1' and . &lt;= '5000')" jr:constraintMsg="Value must be between 1 and 5000"/>
      <bind nodeset="/data/billing_period_start_date" type="date" required="true()"/>
      <bind nodeset="/data/billing_period_end_date" type="date" required="true()"/>
    </model>
  </h:head>
  <h:body>
    <input ref="/data/customer_mobile">
      <label ref="jr:itext('/data/customer_mobile:label')"/>
      <hint ref="jr:itext('/data/customer_mobile:hint')"/>
    </input>
    <input ref="/data/bill_amount">
      <label ref="jr:itext('/data/bill_amount:label')"/>
    </input>
    <input ref="/data/billing_period_start_date">
      <label ref="jr:itext('/data/billing_period_start_date:label')"/>
    </input>
    <input ref="/data/billing_period_end_date">
      <label ref="jr:itext('/data/billing_period_end_date:label')"/>
    </input>
  </h:body>
</h:html>
"""
    response = Response(xml, mimetype='text/xml')
    response.headers['X-OpenRosa-Version'] = '1'

    return response


@app.route('/submission',methods=['HEAD','POST','GET'])
def submission():
    print request.headers
    if request.environ['REQUEST_METHOD'] == 'HEAD':
        response = make_response(render_template('head_request.txt'))
        response.headers['X-OpenRosa-Version'] = '1'
        return response, 204
    elif request.environ['REQUEST_METHOD'] == 'POST':
        xml = ""
        upFile = request.files['xml_submission_file']
        print upFile.name
        xml = upFile.read()
        print xml
    

        #return response
        response = make_response(render_template('home.html'))
        response.headers['X-OpenRosa-Version'] = '1'
        return response, 201
    elif request.environ['REQUEST_METHOD'] == 'GET':
        response = make_response(render_template('home.html'))
        return response, 200



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')