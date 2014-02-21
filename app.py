#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" app.py

Flask application instantiation/routing
"""
__author__ = 'Scott Burns <scott.s.burns@vanderbilt.edu>'
__copyright__ = 'Copyright 2013 Vanderbilt University. All Rights Reserved'

from os import environ

from flask import Flask, render_template, Markup

app = Flask(__name__)
app.debug = False  # others can override, but make sure we're safe by default

from data import get_raw, table_from_groupby

index_url = environ.get('VXHR_INDEX', '/')
v1_url = '{}v1'.format(index_url) if index_url.endswith('/') else \
    '{}/v1'.format(index_url)


@app.route(index_url)
@app.route(v1_url)
def index():
    report_loop = zip(['Project by Module by Version', 'PI by Module', 'Module by Version'],
        [['project_pi', 'module', 'version'], ['pi', 'module'], ['module', 'version']],
        [{'level': 0}, {'level': 0, 'ascending': True}, {}])
    reports = []
    try:
        raw = get_raw()
        for name, gb_columns, sort_kwargs in report_loop:
            unescaped = table_from_groupby(raw, gb_columns, sort_kwargs)
            rep = (name, Markup(unescaped))
            reports.append(rep)
    except Exception as e:
        print e
        reports = [('Uh oh', error_message(e))]
    return render_template('report_v1.html', reports=reports)


def error_message(e):
    unescaped = '<p><strong>Something bad happened</strong>{}</p>'.format(e)
    return Markup(unescaped)