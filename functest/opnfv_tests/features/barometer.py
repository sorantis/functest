#!/usr/bin/python
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0

from baro_tests import collectd

import functest.core.feature as base


class BarometerCollectd(base.Feature):
    '''
    Class for executing barometercollectd testcase.
    '''

    def __init__(self, case_name='barometercollectd'):
        super(BarometerCollectd, self).__init__(project='barometer',
                                                case_name=case_name,
                                                repo='dir_repo_barometer')

    def execute(self):
        return collectd.main(self.logger)
