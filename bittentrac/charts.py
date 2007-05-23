# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8
# =============================================================================
# $Id: charts.py 12 2007-05-23 22:07:56Z s0undt3ch $
# =============================================================================
#             $URL: http://bitten.ufsoft.org/svn/BittenExtraTrac/trunk/bittentrac/charts.py $
# $LastChangedDate: 2007-05-23 23:07:56 +0100 (Wed, 23 May 2007) $
#             $Rev: 12 $
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
  SUM(CASE WHEN item_cat.value='ignored' THEN 1 ELSE 0 END) AS ignored,
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
        for rev, platform, fail, err, warn, ref, conv, ign, score in cursor:
            self.log.debug(rev, platform, fail, err, warn, ref, conv, ign, score)
            if rev != prev_rev:
                if score == None:
                    score = 0
#                else:
#                    score *= 10.0
                scores.append([rev, fail, err, warn, ref, conv, ign, score])
            prev_rev = rev

        self.log.debug(scores)

        req.hdf['chart.title'] = 'PyLint'
        labels = ['[%s]' % item[0] for item in scores]
        score = [item[7]*10.0 for item in scores]
        fatal = [item[1] for item in scores]
        error = [item[2] for item in scores]
        warning = [item[3] for item in scores]
        refactor = [item[4] for item in scores]
        convention = [item[5] for item in scores]
        ignored = [item[6] for item in scores]
        req.hdf['chart.data'] = [
            [''] + labels,
            ['Score'] + score,
            ['Fatal'] + fatal,
            ['Error'] + error,
            ['Warning'] + warning,
            ['Refactor'] + refactor,
            ['Convention'] + convention,
            ['Ignored'] + ignored,
        ]
        score = [item[7] for item in scores]
        req.hdf['chart.real_data'] = [
            [''] + labels,
            ['Score'] + score,
            ['Fatal'] + fatal,
            ['Error'] + error,
            ['Warning'] + warning,
            ['Refactor'] + refactor,
            ['Convention'] + convention,
            ['Ignored'] + ignored,
        ]
        return 'bittentrac_pylint_chart.cs'
