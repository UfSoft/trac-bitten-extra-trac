# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8
# =============================================================================
# $Id: charts.py 10 2007-02-25 23:02:15Z s0undt3ch $
# =============================================================================
#             $URL: http://bitten.ufsoft.org/svn/BittenExtraTrac/trunk/bittentrac/charts.py $
# $LastChangedDate: 2007-02-25 23:02:15 +0000 (Sun, 25 Feb 2007) $
#             $Rev: 10 $
#   $LastChangedBy: s0undt3ch $
# =============================================================================
# Copyright (C) 2006 Ufsoft.org - Pedro Algarvio <ufs@ufsoft.org>
#
# Please view LICENSE for additional licensing information.
# =============================================================================

from trac.core import *
from bitten.trac_ext.api import IReportChartGenerator

class PyLintMessagesChart(Component):
    implements(IReportChartGenerator)

    # IReportChartGenerator methods
    def get_supported_categories(self):
        return ['pylint']

    def generate_chart_data(self, req, config, category):
        assert category == 'pylint'

        db = self.env.get_db_cnx()
        cursor = db.cursor()
        cursor.execute("""
SELECT build.rev, build.platform,
  SUM(CASE WHEN item_cat.value='fatal' THEN 1 ELSE 0 END) AS fatal,
  SUM(CASE WHEN item_cat.value='error' THEN 1 ELSE 0 END) AS errors,
  SUM(CASE WHEN item_cat.value='warning' THEN 1 ELSE 0 END) AS warnings,
  SUM(CASE WHEN item_cat.value='refactor' THEN 1 ELSE 0 END) AS refactors,
  SUM(CASE WHEN item_cat.value='convention' THEN 1 ELSE 0 END) AS convention,
  MAX(CAST(item_score.value AS float)) AS status
FROM bitten_build AS build
 LEFT OUTER JOIN bitten_report AS report ON (report.build=build.id)
LEFT OUTER JOIN bitten_report_item AS item_cat
  ON (item_cat.report=report.id AND item_cat.name='category')
 LEFT OUTER JOIN bitten_report_item AS item_score
  ON (item_score.report=report.id AND item_score.name='score')
WHERE build.config=%s AND report.category='pylint'
GROUP BY build.rev_time, build.rev, build.platform, item_score.value
ORDER BY build.rev_time, build.platform""", (config.name,))

        prev_rev = None
        scores = []
        for rev, platform, fail, err, warn, ref, conv, score in cursor:
            if rev != prev_rev:
                if score == None:
                    score = 0
#                else:
#                    score *= 10.0
                scores.append([rev, fail, err, warn, ref, conv, score])
            prev_rev = rev

        self.log.debug(scores)

        req.hdf['chart.title'] = 'PyLint'
        req.hdf['chart.data'] = [
            [''] + ['[%s]' % item[0] for item in scores],
            ['Score'] + [item[6]*10.0 for item in scores],
            ['Fatal'] + [item[1] for item in scores],
            ['Error'] + [item[2] for item in scores],
            ['Warning'] + [item[3] for item in scores],
            ['Refactor'] + [item[4] for item in scores],
            ['Convention'] + [item[5] for item in scores]
        ]
        req.hdf['chart.real_data'] = [
            [''] + ['[%s]' % item[0] for item in scores],
            ['Score'] + [item[6] for item in scores],
            ['Fatal'] + [item[1] for item in scores],
            ['Error'] + [item[2] for item in scores],
            ['Warning'] + [item[3] for item in scores],
            ['Refactor'] + [item[4] for item in scores],
            ['Convention'] + [item[5] for item in scores]
        ]
        return 'bittentrac_pylint_chart.cs'
