#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" test_data.py

Test data functions
"""
__author__ = 'Scott Burns <scott.s.burns@vanderbilt.edu>'
__copyright__ = 'Copyright 2014 Vanderbilt University. All Rights Reserved'

import pandas as pd
from datetime import datetime

from vxhr import data


test_data = """record_id,spider_module_name,spider_module_version,date,xnat_project,hostname,pi_lastname,job_information_complete
"AbOrganCT2-2014-02-13_18_02_59_755535","Preview_NIFTI","v0","2014-02-13 18:02:59.755535","AbOrganCT2","poplar.vampire","Landman",0
"AbOrganCT2-2014-02-13_22_02_30_697331","dcm2nii","v0","2014-02-13 22:02:30.697331","AbOrganCT2","poplar.vampire","Landman",0
"AbOrganCT2-2014-02-13_22_03_05_954337","Preview_NIFTI","v0","2014-02-13 22:03:05.954337","AbOrganCT2","poplar.vampire","Landman",0
"AbOrganCT2-2014-02-14_02_02_46_954597","dcm2nii","v0","2014-02-14 02:02:46.954597","AbOrganCT2","poplar.vampire","Landman",0
"AbOrganCT2-2014-02-14_02_03_20_744525","Preview_NIFTI","v0","2014-02-14 02:03:20.744525","AbOrganCT2","poplar.vampire","Landman",0
"AbOrganCT2-2014-02-14_06_02_27_872095","dcm2nii","v0","2014-02-14 06:02:27.872095","AbOrganCT2","poplar.vampire","Landman",0
"AbOrganCT2-2014-02-14_06_03_00_664993","Preview_NIFTI","v0","2014-02-14 06:03:00.664993","AbOrganCT2","poplar.vampire","Landman",0
"AbOrganCT2-2014-02-14_10_02_27_322119","dcm2nii","v0","2014-02-14 10:02:27.322119","AbOrganCT2","poplar.vampire","Landman",0
"AbOrganCT2-2014-02-14_10_03_00_387632","Preview_NIFTI","v0","2014-02-14 10:03:00.387632","AbOrganCT2","poplar.vampire","Landman",0
"AbOrganCT2-2014-02-14_14_02_28_002463","dcm2nii","v0","2014-02-14 14:02:28.002463","AbOrganCT2","poplar.vampire","Landman",0
"AbOrganCT2-2014-02-14_14_03_00_959743","Preview_NIFTI","v0","2014-02-14 14:03:00.959743","AbOrganCT2","poplar.vampire","Landman",0
"AbOrganCT2-2014-02-14_18_02_18_755007","dcm2nii","v0","2014-02-14 18:02:18.755007","AbOrganCT2","poplar.vampire","Landman",0
"AbOrganCT2-2014-02-14_18_02_51_652622","Preview_NIFTI","v0","2014-02-14 18:02:51.652622","AbOrganCT2","poplar.vampire","Landman",0
"AbOrganCT2-2014-02-14_22_02_21_254663","dcm2nii","v0","2014-02-14 22:02:21.254663","AbOrganCT2","poplar.vampire","Landman",0
"AbOrganCT2-2014-02-14_22_02_54_579798","Preview_NIFTI","v0","2014-02-14 22:02:54.579798","AbOrganCT2","poplar.vampire","Landman",0
"BLSA-2014-02-05_12_00_05_377336","Preview_NIFTI","v0","2014-02-05 12:00:05.377336","BLSA","poplar.vampire","Landman",0
"BLSA-2014-02-05_12_00_29_909053","Sync_REDCap","v0","2014-02-05 12:00:29.909053","BLSA","poplar.vampire","Landman",0
"BLSA-2014-02-05_19_18_15_980990","FreeSurfer","v0","2014-02-05 19:18:15.980990","BLSA","poplar.vampire","Landman",0
"BLSA-2014-02-05_19_38_03_861641","White_Matter_Stamper","v0","2014-02-05 19:38:03.861641","BLSA","poplar.vampire","Landman",0
"BLSA-2014-02-05_20_48_45_430108","White_Matter_Stamper","v0","2014-02-05 20:48:45.430108","BLSA","poplar.vampire","Landman",0
"""

def test_last_launch():
    d1, d2, d3 = test_list = [datetime(2013, 1, 30),
                              datetime(2012, 1, 30),
                              datetime(2014, 1, 30)]
    assert data.last_launch(test_list) == d3

def test_df_from_csv():
    assert isinstance(data.df_from_csv(test_data), pd.DataFrame)

def test_xfm_datetime():
    xfm = data.xfm_df(data.df_from_csv(test_data))
    assert isinstance(xfm.date[0], datetime)
    required = ['project', 'date', 'module', 'version', 'pi', 'project_pi']
    for req in required:
        assert req in xfm
