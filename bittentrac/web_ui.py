# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8
# =============================================================================
# $Id: web_ui.py 4 2007-02-10 23:28:33Z s0undt3ch $
# =============================================================================
#             $URL: http://bitten.ufsoft.org/svn/BittenExtraTrac/trunk/bittentrac/web_ui.py $
# $LastChangedDate: 2007-02-10 23:28:33 +0000 (Sat, 10 Feb 2007) $
#             $Rev: 4 $
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


class BittenTracTemplates(Component):
    implements(ITemplateProvider, IRequestFilter)

    # ITemplateProvider methods

    def get_htdocs_dirs(self):
        return [(
            'bittentrac',
            pkg_resources.resource_filename(__name__, 'htdocs')
        )]

    def get_templates_dirs(self):
        return [pkg_resources.resource_filename(__name__, 'templates')]

    # IRequestFilter methods
    def pre_process_request(self, req, handler):
        return handler

    def post_process_request(self, req, template, content_type):
        if req.path_info.startswith('/build'):
            add_stylesheet(req, 'bittentrac/bittentrac.css')


class BittenTracJS(Component):
    implements(IRequestFilter)

    # IRequestFilter methods
    def pre_process_request(self, req, handler):
        return handler

    def post_process_request(self, req, template, content_type):
        if req.path_info.startswith('/build'):
            add_script(req, 'bittentrac/jquery-latest.js')
            add_script(req, 'bittentrac/jquery.tablesorter.js')
            add_script(req, 'bittentrac/jquery.hovertip.js')
        return template, content_type
