# coding: utf-8
"""
   Copyright 2019 Alibaba Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import opensearch.generated.OpenSearchSearcher.constants
from opensearch.generated.OpenSearchSearcher.ttypes import Order
from opensearch.generated.OpenSearchSearcher.ttypes import SearchFormat

class ClauseParamsBuilder(object):
    CONFIG_KEY = 'config'
    QUERY_KEY = 'query'
    SORT_KEY = 'sort'
    DISTINCT_KEY = 'distinct'
    AGGREGATE_KEY = 'aggregate'
    FILTER_KEY = 'filter'
    KVPAIRS = 'kvpairs'

    CLAUSE_SEPARATOR = '&&'
    KV_SEPARATOR = '='
    CLAUSE_CONFIG_SEPARATOR = ','
    CLAUSE_CONFIG_KV_SEPARATOR = ':'

    CLAUSE_SORT_SEPARATOR = ';'

    CLAUSE_DISTINCT_KV_SEPARATOR = ':'
    CLAUSE_DISTINCT_SEPARATOR = ';'
    CLAUSE_DISTINCT_SUB_SEPARATOR = ','

    CLAUSE_AGGREGATE_KV_SEPARATOR = ':'
    CLAUSE_AGGREGATE_SEPARATOR = ';'
    CLAUSE_AGGREGATE_SUB_SEPARATOR = ','

    CONFIG_CLAUSE_START = 'CONFIG_CLAUSE_START'
    CONFIG_CLAUSE_HIT = 'CONFIG_CLAUSE_HIT'
    CONFIG_CLAUSE_RERANK_SIZE = 'CONFIG_CLAUSE_RERANK_SIZE'
    CONFIG_CLAUSE_FORMAT = 'CONFIG_CLAUSE_FORMAT'

    DISTINCT_CLAUSE_DIST_KEY = 'DISTINCT_CLAUSE_DIST_KEY'
    DISTINCT_CLAUSE_DIST_COUNT = 'DISTINCT_CLAUSE_DIST_COUNT'
    DISTINCT_CLAUSE_DIST_TIMES = 'DISTINCT_CLAUSE_DIST_TIMES'
    DISTINCT_CLAUSE_RESERVED = 'DISTINCT_CLAUSE_RESERVED'
    DISTINCT_CLAUSE_DIST_FILTER = 'DISTINCT_CLAUSE_DIST_FILTER'
    DISTINCT_CLAUSE_UPDATE_TOTAL_HIT = 'DISTINCT_CLAUSE_UPDATE_TOTAL_HIT'
    DISTINCT_CLAUSE_GRADE = 'DISTINCT_CLAUSE_GRADE'

    DISTINCT_KEY_MAP = {}

    AGGREGATE_CLAUSE_GROUP_KEY = 'AGGREGATE_CLAUSE_GROUP_KEY'
    AGGREGATE_CLAUSE_AGG_FUN = 'AGGREGATE_CLAUSE_AGG_FUN'
    AGGREGATE_CLAUSE_RANGE = 'AGGREGATE_CLAUSE_RANGE'
    AGGREGATE_CLAUSE_MAX_GROUP = 'AGGREGATE_CLAUSE_MAX_GROUP'
    AGGREGATE_CLAUSE_AGG_FILTER = 'AGGREGATE_CLAUSE_AGG_FILTER'
    AGGREGATE_CLAUSE_AGG_SAMPLER_THRESHOLD = 'AGGREGATE_CLAUSE_AGG_SAMPLER_THRESHOLD'
    AGGREGATE_CLAUSE_AGG_SAMPLER_STEP = 'AGGREGATE_CLAUSE_AGG_SAMPLER_STEP'

    AGGREGATE_KEY_MAP = {}

    def __init__(self, search_params):
        self.__params = search_params
        self.__clauses = {}
        self.DISTINCT_KEY_MAP = {
            'key': self.DISTINCT_CLAUSE_DIST_KEY,
            'distCount': self.DISTINCT_CLAUSE_DIST_COUNT,
            'distTimes': self.DISTINCT_CLAUSE_DIST_TIMES,
            'reserved': self.DISTINCT_CLAUSE_RESERVED,
            'distFilter': self.DISTINCT_CLAUSE_DIST_FILTER,
            'updateTotalHit': self.DISTINCT_CLAUSE_UPDATE_TOTAL_HIT,
            'grade': self.DISTINCT_CLAUSE_GRADE
        }
        self.AGGREGATE_KEY_MAP = {
            'groupKey': self.AGGREGATE_CLAUSE_GROUP_KEY,
            'aggFun': self.AGGREGATE_CLAUSE_AGG_FUN,
            'range': self.AGGREGATE_CLAUSE_RANGE,
            'maxGroup': self.AGGREGATE_CLAUSE_MAX_GROUP,
            'aggFilter': self.AGGREGATE_CLAUSE_AGG_FILTER,
            'aggSamplerThresHold': self.AGGREGATE_CLAUSE_AGG_SAMPLER_THRESHOLD,
            'aggSamplerStep': self.AGGREGATE_CLAUSE_AGG_SAMPLER_STEP
        }

    def __build_config_clause(self):
        config_list = [];
        if (self.__params.config.start != None):
            config = CONFIG_CLAUSE_START + self.CLAUSE_CONFIG_KV_SEPARATOR + self.__params.config.start
            config_list.append(config)
        if (self.__params.config.hits != None):
            config = CONFIG_CLAUSE_HIT + self.CLAUSE_CONFIG_KV_SEPARATOR + self.__params.config.hits
            config_list.append(config)
        if (self.__params.config.searchFormat != None):
            lowercase_format = SearchFormat._VALUES_TO_NAMES[self.__params.config.searchFormat].tolower()
            config = CONFIG_CLAUSE_FORMAT + self.CLAUSE_CONFIG_KV_SEPARATOR + lowercase_format
            config_list.append(config)
        if (self.__params.config.reRankSize != None):
            config = CONFIG_CLAUSE_RERANK_SIZE + self.CLAUSE_CONFIG_KV_SEPARATOR + self.__params.config.reRankSize
            config_list.append(config)
        if (self.__params.config.customConfig != None):
            for k in self.__params.config.customConfig:
                config = k + self.CLAUSE_CONFIG_KV_SEPARATOR + self.__params.config.customConfig[k]
                config_list.append(config)

        self.__clauses[self.CONFIG_KEY] = self.CLAUSE_CONFIG_SEPARATOR.join(config_list)

    def __build_config_clause(self):
        if (self.__params.query != None):
            self.__clauses[self.QUERY_KEY] = self.__params.query

    def __build_sort_clause(self):
        if (self.__params.sort.sortFields != None):
            sort_list = []
            for sort_field in self.__params.sort.sortFields:
                order_string = Order._VALUES_TO_NAMES[sort_field.order]
                constant_name = 'SORT_CLAUSE_' + order_string
                sort_list.append(globals()[constant_name] + sort_field.field)

            self.__clauses[self.CONFIG_KEY] = self.CLAUSE_CONFIG_SEPARATOR.join(sort_list)


    def __build_filter_clause(self):
        if (self.__params.filter != None):
            self.__clauses[self.FILTER_KEY] = self.__params.filter

    def __build_distinct_clause(self):
        if (self.__params.distincts != None):
            distincts = []
            for distinct in self.__params.distincts:
                if (distinct.key == None):
                    continue

                sub_clause_list = []
                for k in self.DISTINCT_KEY_MAP:
                    if (distinct.get(k) != None):
                        v = self.DISTINCT_KEY_MAP[k]
                        sub_clause = globals()[v] + self.CLAUSE_AGGREGATE_KV_SEPARATOR + distinct.get(k)
                        sub_clause_list.append(sub_clause)

                clause = self.CLAUSE_DISTINCT_SUB_SEPARATOR.join(sub_clause_list)
                distincts.append(clause)

            self.__clauses[self.DISTINCT_KEY] = self.CLAUSE_DISTINCT_SEPARATOR.join(distincts)

    def __build_aggregate_clause(self):
        if (self.__params.aggregates != None):
            aggregates = []
            for aggregate in self.__params.aggregates:
                if (aggregate.groupKey == None or aggregate.aggFun == None):
                    continue

                sub_clause_list = []
                for k in self.AGGREGATE_KEY_MAP:
                    if (aggregate.get(k) != None):
                        v = self.AGGREGATE_KEY_MAP[k]
                        sub_clause = globals()[v] + self.CLAUSE_AGGREGATE_KV_SEPARATOR + aggregate.get(k)
                        sub_clause_list.append(sub_clause)

                clause = self.CLAUSE_AGGREGATE_SUB_SEPARATOR.join(sub_clause_list)
                aggregates.append(clause)

            self.__clauses[self.AGGREGATE_KEY] = self.CLAUSE_AGGREGATE_SEPARATOR.join(aggregates)

    def __build_kvpairs_clause(self):
        if (self.__params.kvpairs != None):
            self.__clauses[self.KVPAIRS] = self.__params.kvpairs

    def get_clauses_string(self):
        """获取搜索条件字符串
        :return: str
        """
        self.__build_config_clause()
        self.__build_query_clause()
        self.__build_sort_clause()
        self.__build_filter_clause()
        self.__build_distinct_clause()
        self.__build_aggregate_clause()
        self.__build_kvpairs_clause()

        clauses = [];
        for clause_key in self.__clauses:
            clause = clause_key + self.KV_SEPARATOR + self.__clauses[clause_key]
            clauses.append(clause)

        return self.CLAUSE_SEPARATOR.join(clauses)
