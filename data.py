#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" data.py

Functions for grabbing/manipulating/reporting on data
"""
__author__ = 'Scott Burns <scott.s.burns@vanderbilt.edu>'
__copyright__ = 'Copyright 2014 Vanderbilt University. All Rights Reserved'

import os

import pandas as pd
from redcap import Project

try:
    RCURL = os.environ['VXHR_RCURL']
    RCAPI = os.environ['VXHR_RCTOKEN']
except KeyError as e:
    print("You must set %s" % str(e))
    raise

def get_raw():
    """Top-level function.Use to get a DataFrame from the redcap project

    Callers **should** catch errors"""
    return xfm_df(df_from_csv(csv_from_redcap()))

# HELPERS

def combine_project_pi(record):
    "Takes a record, returns a string like PROJECT_LASTNAME"
    return '{} ({})'.format(record['project'], record['pi'])


def csv_from_redcap():
    p = Project(RCURL, RCAPI)
    return p.export_records(format='csv')


def df_from_csv(csv):
    from StringIO import StringIO
    buf = StringIO(csv)
    return pd.DataFrame.from_csv(buf)


def xfm_df(df):
    rename = {'xnat_project': 'project',
              'pi_lastname': 'pi',
              'spider_module_version': 'version',
              'spider_module_name': 'module'}
    df.date = pd.to_datetime(df.date)
    df.rename(columns=rename, inplace=True)
    df['module'] = df.module.apply(lambda x: x.upper())
    df['project_pi'] = df.apply(combine_project_pi, axis=1)
    return df


def last_launch(g):
    """Take a list-like object `g` of datetimes, sort descending
    & take the first element"""
    return sorted(g, reverse=True)[0]


def table_from_groupby(raw, gb_columns, sort_kwargs=None):
    to_agg = {'Last Launched': last_launch, 'Count': pd.Series.nunique}
    df = df_from_agg(raw, gb_columns, to_agg)
    if sort_kwargs:
        sort_kwargs['inplace'] = True
        df.sortlevel(**sort_kwargs)
    return table_from_df(df)


def df_from_agg(raw, gb_columns, to_agg):
    df = raw.groupby(gb_columns).date.agg(to_agg)
    # because we're agg'ing on a datetime, 'Count' needs to be coerced to int
    df.Count = df.Count.astype('int64')
    return df


def table_from_df(df):
    return df.to_html(classes=["table", "table-striped", "table-bordered"])