"""
Copyright (C) 2004-2015 Pivotal Software, Inc. All rights reserved.

This program and the accompanying materials are made available under
the terms of the under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import tinctest
from tinctest.models.scenario import ScenarioTestCase
from mpp.gpdb.tests.storage.aoco_compression import GenerateSqls

class AOCOCompressionTestCase(ScenarioTestCase):
    """
    @gucs gp_create_table_random_default_distribution=off
    @product_version gpdb: [4.3-]
    """



    @classmethod
    def setUpClass(cls):
        gensql = GenerateSqls()
        gensql.generate_sqls()


    def test_aoco_large_block(self):
        '''
        @data_provider test_types_large
        '''
        test_list1 = []
        test_list1.append("mpp.gpdb.tests.storage.aoco_compression.test_runsqls.%s" % self.test_data[1][0])
        self.test_case_scenario.append(test_list1)

    def test_validation(self):
        '''
        Check catakog and checkmirrorintegrity
        note: Seperating this out to not run as part of every test
        '''
        test_list1 = []
        test_list1.append("mpp.gpdb.tests.storage.lib.dbstate.DbStateClass.run_validation")
        self.test_case_scenario.append(test_list1)


@tinctest.dataProvider('test_types_large')
def test_data_provider():
    data = {'test_01_3_co_create_storage_directive_large':['co_create_storage_directive_large_2G_zlib'],
            'test_01_4_co_create_storage_directive_large':['co_create_storage_directive_large_2G_quick_rle'],
            'test_01_6_co_create_storage_directive_large':['co_create_storage_directive_large_2G_zlib_2'],
            'test_02_3_co_create_column_reference_default_large':['co_create_column_reference_default_large_2G_zlib'],
            'test_02_4_co_create_column_reference_default_large':['co_create_column_reference_default_large_2G_quick_rle'],
            'test_02_6_co_create_column_reference_default_large':['co_create_column_reference_default_large_2G_zlib_2'],
            'test_03_3_co_create_column_reference_column_large':['co_create_column_reference_column_large_2G_zlib'],
            'test_03_4_co_create_column_reference_column_large':['co_create_column_reference_column_large_2G_quick_rle'],
            'test_03_6_co_create_column_reference_column_large':['co_create_column_reference_column_large_2G_zlib_2'],
            'test_04_3_ao_create_with_row_large':['ao_create_with_row_large_2G_zlib'],
            'test_04_4_ao_create_with_row_large':['ao_create_with_row_large_2G_quick_rle'],
           }
    return data


