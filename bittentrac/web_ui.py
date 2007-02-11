# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8
# =============================================================================
# $Id: web_ui.py 6 2007-02-11 00:00:47Z s0undt3ch $
# =============================================================================
#             $URL: http://bitten.ufsoft.org/svn/BittenExtraTrac/trunk/bittentrac/web_ui.py $
# $LastChangedDate: 2007-02-11 00:00:47 +0000 (Sun, 11 Feb 2007) $
#             $Rev: 6 $
#   $LastChangedBy: s0undt3ch $
# =============================================================================
# Copyright (C) 2006 Ufsoft.org - Pedro Algarvio <ufs@ufsoft.org>
#
# Please view LICENSE for additional licensing information.
# =============================================================================

import pkg_resources
from trac.core import *
from trac.web.chrome import add_script, add_stylesheet, ITemplateProvider
from trac.web.api import IRequestFilter

class BittenTracChrome(Component):
    implements(ITemplateProvider, IRequestFilter)

    # ITemplateProvider methods
    def get_htdocs_dirs(self):
        return [(
            'bittentrac',
            pkg_resources.resource_filename(__name__, 'htdocs')
        )]

    def get_templates_dirs(self):
        return [pkg_resources.resource_filename(__name__, 'templates')]

    def pre_process_request(self, req, handler):
        return handler

    def post_process_request(self, req, template, content_type):
        if req.path_info.startswith('/build'):
            add_stylesheet(req, 'bittentrac/bittentrac.css')
            add_script(req, 'bittentrac/jquery-latest.js')
            add_script(req, 'bittentrac/jquery.tablesorter.js')
            add_script(req, 'bittentrac/jquery.hovertip.js')
        return template, content_type
