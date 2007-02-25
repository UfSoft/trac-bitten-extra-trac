#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8
# =============================================================================
# $Id: setup.py 10 2007-02-25 23:02:15Z s0undt3ch $
# =============================================================================
#             $URL: http://bitten.ufsoft.org/svn/BittenExtraTrac/trunk/setup.py $
# $LastChangedDate: 2007-02-25 23:02:15 +0000 (Sun, 25 Feb 2007) $
#             $Rev: 10 $
#   $LastChangedBy: s0undt3ch $
# =============================================================================
# Copyright (C) 2006 Ufsoft.org - Pedro Algarvio <ufs@ufsoft.org>
#
# Please view LICENSE for additional licensing information.
# =============================================================================

from setuptools import setup, find_packages

NS = 'http://bitten.cmlenz.net/tools/bet#'

setup(
    name='BittenExtraTrac',
    version='0.1',
    author='Pedro Algarvio',
    author_email = 'ufs@ufsoft.org',
    description = 'Bitten Trac plugin',
    license = 'BSD',
    packages = find_packages(),
    install_requires=['bitten==dev,>=0.6dev-r378'],
    entry_points = {
        'trac.plugins': [
            'bittentrac.sumarizers = bittentrac.sumarizers',
            'bittentrac.web_ui = bittentrac.web_ui',
            'bittentrac.charts = bittentrac.charts'
        ],
    'bitten.recipe_commands': [
            NS + 'unittest = bittentrac.plugbitten:unittest',
            NS + 'coverage = bittentrac.plugbitten:coverage',
            NS + 'pylint = bittentrac.plugbitten:nblint'
        ]
    }
)
