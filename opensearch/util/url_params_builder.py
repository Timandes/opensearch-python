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
from opensearch.generated.OpenSearchSearcher.ttypes import DeepPaging
from opensearch.generated.OpenSearchSearcher.ttypes import SearchType
import opensearch.util

class UrlParamsBuilder(object):

    QUERY = 'query'
    FORMAT = 'format'
    FIRST_RANK_NAME = 'first_rank_name'
    SECOND_RANK_NAME = 'second_rank_name'
    SUMMARY = 'summary'
    FETCH_FIELDS = 'fetch_fields'
    QP = 'qp'
    DISABLE = 'disable'
    ROUTE_VALUE = 'route_value'
    SCROLL_EXPIRE = 'scroll'
    SCROLL_ID = 'scroll_id'
    SEARCH_TYPE = 'search_type'
    ABTEST = "abtest"
    USER_ID = "user_id"
    RAW_QUERY = "raw_query"

    FETCH_FIELDS_SEPARATOR = ';'
    QP_SEPARATOR = ','
    DISABLE_FUNCTIONS_SEPARATOR = ';'

    SUMMARY_SEPARATOR = ';'
    SUMMARY_SUB_SEPARATOR = ','
    SUMMARY_KV_SEPARATOR = ':'

    SUMMARY_KEY_MAP = {
        'summary_field': 'SUMMARY_PARAM_SUMMARY_FIELD',
        'summary_len': 'SUMMARY_PARAM_SUMMARY_LEN',
        'summary_ellipsis': 'SUMMARY_PARAM_SUMMARY_ELLIPSIS',
        'summary_snippet': 'SUMMARY_PARAM_SUMMARY_SNIPPET',
        'summary_element': 'SUMMARY_PARAM_SUMMARY_ELEMENT',
        'summary_element_prefix': 'SUMMARY_PARAM_SUMMARY_ELEMENT_PREFIX',
        'summary_element_postfix': 'SUMMARY_PARAM_SUMMARY_ELEMENT_POSTFIX'
    }

    SEARCH_TYPE_SCAN = 'scan'

    ABTEST_SEPARATOR = ';'
    ABTEST_SUB_SEPARATOR = ','
    ABTEST_KV_SEPARATOR = ':'

    ABTEST_KEY_MAP = {
        'sceneTag': 'ABTEST_PARAM_SCENE_TAG',
        'flowDivider': 'ABTEST_PARAM_FLOW_DIVIDER',
    }

    def __init__(self, search_params):
        self.__init_query(search_params)
        self.__init_scroll(search_params)
        self.__init_rank(search_params)
        self.__init_fetch_fields(search_params)
        self.__init_summary(search_params)
        self.__init_query_processor(search_params)
        self.__init_disable_functions(search_params)
        self.__init_route_value(search_params)
        self.__init_custom_params(search_params)
        self.__init_abtest(search_params)
        self.__init_user_id(search_params)
        self.__init_raw_query(search_params)

    def __init_query(self, search_params):
        builder = ClauseParamsBuilder(search_params)
        self.__params[self.QUERY] = builder.get_clauses_string()

    def __init_scroll(self, search_params):
        if (search_params.deepPaging != None and search_params.deepPaging is DeepPaging):
            if (search_params.deepPaging.scrollId != None and search_params.deepPaging.scrollId != ""):
                self.__params[self.SCROLL_ID] = search_params.deepPaging.scrollId
            else:
                self.__params[self.SEARCH_TYPE] = self.SEARCH_TYPE_SCAN
            self.__params[self.SCROLL_EXPIRE] = search_params.deepPaging.scrollExpire

    def __init_rank(self, search_params):
        if (search_params.rank.firstRankName != None):
            self.__params[self.FIRST_RANK_NAME] = search_params.rank.firstRankName
        if (search_params.rank.secondRankName != None):
            self.__params[self.SECOND_RANK_NAME] = search_params.rank.secondRankName

    def __init_fetch_fields(self, search_params):
        if (search_params.config.fetchFields != None):
            self.__params[self.FETCH_FIELDS] = self.FETCH_FIELDS_SEPARATOR.join(search_params.config.fetchFields)

    def __init_summary(self, search_params):
        if (search_params.summaries != None):
            summaries = []
            for summary in search_params.summaries:
                if summary == None:
                    continue

                sub_clause_list = []
                for k in self.SUMMARY_KEY_MAP:
                    if (summary.get(k) != None):
                        v = self.SUMMARY_KEY_MAP[k]
                        sub_clause = globals()[v] + self.SUMMARY_KV_SEPARATOR + summary.get(k)
                        sub_clause_list.append(sub_clause)

                clause = self.SUMMARY_SUB_SEPARATOR.join(sub_clause_list)
                summaries.append(clause)

            self.__params[self.SUMMARY] = self.SUMMARY_SEPARATOR.join(summaries)

    def __init_query_processor(self, search_params):
        if (search_params.queryProcessorNames != None):
            self.__params[self.QP] = self.QP_SEPARATOR.join(search_params.queryProcessorNames)

    def __init_disable_functions(self, search_params):
        if (search_params.disableFunctions != None):
            self.__params[self.DISABLE] = self.DISABLE_FUNCTIONS_SEPARATOR.join(search_params.disableFunctions)

    def __init_route_value(self, search_params):
        if (search_params.config.routeValue != None):
            self.__params[self.ROUTE_VALUE] = search_params.config.routeValue

    def __init_custom_params(self, search_params):
        if (search_params.customParam != None):
            for k in search_params.customParam:
                self.__params[k] = search_params.customParam[k]

    def __init_abtest(self, search_params):
        if (search_params.abtest != None):
            abtest = search_params.abtest

            sub_clause_list = []
            for k in self.ABTEST_KEY_MAP:
                if (abtest.get(k) != None):
                    v = self.ABTEST_KEY_MAP[k]
                    sub_clause = globals()[v] + self.ABTEST_KV_SEPARATOR + abtest.get(k)
                    sub_clause_list.append(sub_clause)

            self.__params[self.ABTEST] = self.ABTEST_SUB_SEPARATOR.join(sub_clause_list)

    def __init_user_id(self, search_params):
        if (search_params.userId != None):
            self.__params[self.USER_ID] = search_params.userId

    def __init_raw_query(self, search_params):
        if (search_params.rawQuery != None):
            self.__params[self.RAW_QUERY] = search_params.rawQuery

    def get_http_params(self):
        """获取可用于搜索HTTP请求的参数
        :return: dict
        """
        return self.___params
