#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" vxhr.py

Interface
"""
__author__ = 'Scott Burns <scott.s.burns@vanderbilt.edu>'
__copyright__ = 'Copyright 2014 Vanderbilt University. All Rights Reserved'

import os

from app import app
import data

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('VXHR_PORT', 9000))
    host = os.environ.get('VXHR_HOST', '127.0.0.1')
    app.run(host=host, port=port)