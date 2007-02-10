#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8
# =============================================================================
# $Id: setup.py 4 2007-02-10 23:28:33Z s0undt3ch $
# =============================================================================
#             $URL: http://bitten.ufsoft.org/svn/BittenExtraTrac/trunk/setup.py $
# $LastChangedDate: 2007-02-10 23:28:33 +0000 (Sat, 10 Feb 2007) $
#             $Rev: 4 $
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
            'bittentrac.web_ui = bittentrac.web_ui'
        ],
    'bitten.recipe_commands': [
            NS + 'unittest = bittentrac.plugbitten:unittest',
            NS + 'coverage = bittentrac.plugbitten:coverage',
            NS + 'lint = bittentrac.plugbitten:nblint'
        ]
    }
)
