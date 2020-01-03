#coding utf-8
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

from opensearch.generated.OpenSearchSearcher.ttypes import Abtest
from opensearch.generated.OpenSearchSearcher.ttypes import Aggregate
from opensearch.generated.OpenSearchSearcher.ttypes import Config
from opensearch.generated.OpenSearchSearcher.ttypes import DeepPaging
from opensearch.generated.OpenSearchSearcher.ttypes import Distinct
from opensearch.generated.OpenSearchSearcher.ttypes import SearchFormat
from opensearch.generated.OpenSearchSearcher.ttypes import SearchParams
from opensearch.generated.OpenSearchSearcher.ttypes import Sort
from opensearch.generated.OpenSearchSearcher.ttypes import SortField
from opensearch.generated.OpenSearchSearcher.ttypes import Summary

class SearchParamsBuilder(object):
    SORT_INCREASE   = 1
    SORT_DECREASE   = 0

    def __init__(self):
        config = Config()
        self.__search_params = SearchParams(config=config)

    def build(self):
        return self.__search_params

    def set_start(self, start):
        """设置返回结果的偏移量。
        :param start: 偏移量，范围[0,5000]。
        """
        self.__search_params.config.start = start

    def set_hits(self, hits):
        """设置返回结果的条数。
        :param hits: 返回结果的条数，范围[0,500]。
        """
        self.__search_params.config.hits = hits

    def set_format(self, format_string):
        """设置返回结果的格式。
        :param format_string: 返回结果的格式，有json、fulljson和xml格式。
        """
        uppercase_format = format_string.upper()
        if (uppercase_format in SearchFormat._NAMES_TO_VALUES):
            self.__search_params.config.searchFormat = SearchFormat._NAMES_TO_VALUES[uppercase_format]

    def set_app_names(self, app_names):
        """设置要搜索的应用名称或ID。
        :param app_names: 指定要搜索的应用名称或ID。
        """
        if (type(app_names) == list):
            app_name_list = app_names
        else:
            app_name_list = list()
            app_name_list.append(app_names)
        self.__search_params.config.appNames = app_name_list

    def set_query(self, query):
        """设置搜索关键词。
        :param query: 设置的搜索关键词，格式为：索引名:'关键词' [AND|OR ...]
        """
        self.__search_params.config.query = query

    def set_kv_pairs(self, kv_pairs):
        """设置KVpairs。
        :param kv_pairs: 设置kvpairs。
        """
        self.__search_params.config.kvpairs = kv_pairs

    def set_fetch_fields(self, fetch_fields):
        """设置结果集的返回字段。
        :param fetch_fields: 指定的返回字段的列表，例如array('a', 'b')
        """
        self.__search_params.config.fetchFields = fetch_fields

    def set_route_value(self, route_value):
        """如果分组查询时，指定分组的值。
        :param route_value: 分组字段值。
        """
        self.__search_params.config.routeValue = route_value

    def set_re_rank_size(self, re_rank_size):
        """设置参与精排个数。
        :param re_rank_size: 参与精排个数，范围[0,2000]。
        """
        self.__search_params.rank.reRankSize = re_rank_size

    def set_custom_config(self, key, value):
        """在Config字句中增加自定义的参数。
        :param key: 设定自定义参数名。
        :param value: 设定自定义参数值。
        """
        if (self.__search_params.config.customConfig == None):
            self.__search_params.config.customConfig = {}

        self.__search_params.config.customConfig[key] = value

    def add_filter(self, filter_string, condition="AND"):
        """添加过滤条件。
        :param filter_string: 过滤，例如a>1。
        :param condition: 两个过滤条件的连接符, 例如AND OR等。
        """
        if (self.__search_params.filter == None):
            self.__search_params.filter = filter_string
        else:
            self.__search_params.filter = " " + condition + " " + filter_string

    def set_filter(self, filter_string):
        """设置过滤条件。
        :param filter_string: 过滤，例如a>1 OR b<2。
        """
        self.__search_params.filter = filter_string

    def add_sort(self, field, order=self.SORT_DECREASE):
        """添加排序规则。
        :param field: 排序字段。
        :param order: 排序策略，有降序0或者升序1，默认降序。
        """
        if (self.__search_params.sort == None):
            self.__search_params.sort = Sort()
            self.__search_params.sort.sortFields = []
        sort_field = SortField(field=field, order=order)
        self.__search_params.sort.sortFields.append(sort_field)

    def set_first_rank_name(self, first_rank_name):
        """设置粗排表达式名称。
        :param first_rank_name: 指定的粗排表达式名称。
        """
        self.__search_params.rank.firstRankName = first_rank_name

    def set_second_rank_name(self, second_rank_name):
        """设置精排表达式名称。
        :param second_rank_name: 指定的精排表达式名称。
        """
        self.__search_params.rank.secondRankName = second_rank_name

    def add_aggregate(self, attr):
        """设置聚合配置。
        :param attr: 指定的聚合配置。
        """
        if (self.__search_params.aggregates == None):
            self.__search_params.aggregates = []
        aggregate = Aggregate(attr)
        self.__search_params.aggregates.append(aggregate)

    def add_distinct(self, attr):
        """设置去重配置。
        :param attr: 指定的去重配置。
        """
        if (self.__search_params.distincts == None):
            self.__search_params.distincts = []
        distinct = Distinct(attr)
        self.__search_params.distincts.append(distinct)

    def add_summary(self, meta):
        """设置搜索结果摘要配置。
        :param meta: 指定的摘要字段配置。
        """
        if (self.__search_params.summaries == None):
            self.__search_params.summaries = []
        summary = Summary(meta)
        self.__search_params.summaries.append(summary)

    def add_query_processor(self, qp_name):
        """添加查询分析配置。
        :param qp_name: 指定的QP名称。
        """
        if (self.__search_params.queryProcessorNames == None):
            self.__search_params.queryProcessorNames = []
        self.__search_params.queryProcessorNames.append(qp_name)

    def add_disabled_function(self, disabled_function):
        """添加要关闭的function。
        :param disabled_function: 指定的要关闭的方法名称。
        """
        if (self.__search_params.disableFunctions == None):
            self.__search_params.disableFunctions = []
        self.__search_params.disableFunctions.append(disabled_function)

    def set_custom_param(self, key, value):
        """设置自定义参数。
        :param key: 自定义参数的参数名。
        :param value: 自定义参数的参数值。
        """
        if (self.__search_params.customParam == None):
            self.__search_params.customParam = {}
        self.__search_params.customParam[key] = value

    def set_scroll_expire(self, expired_time):
        """设置扫描数据的过期时间。
        :param expired_time: 设定scroll的过期时间。
        """
        if (self.__search_params.deepPaging == None):
            self.__search_params.deepPaging = DeepPaging()
        self.__search_params.deepPaging.scrollExpire = expired_time

    def set_scroll_id(self, scroll_id):
        """设置扫描数据的scrollId。
        :param scroll_id: 设定scroll的scrollId。
        """
        if (self.__search_params.deepPaging == None):
            self.__search_params.deepPaging = DeepPaging()
        self.__search_params.deepPaging.scrollId = scroll_id

    def set_scene_tag(self, scene_tag):
        """设置abtest数据的sceneTag。
        SceneTag 为场景标签。
        :param scene_tag: 设定abtest的sceneTag。
        """
        if (self.__search_params.abtest == None):
            self.__search_params.abtest = Abtest()
        self.__search_params.abtest.sceneTag = scene_tag

    def set_flow_divider(self, flow_divider):
        """设置abtest数据的flowDivider。
        FlowDivider 为流量分配标识。
        :param flow_divider: 设定abtest的flowDivider。
        """
        if (self.__search_params.abtest == None):
            self.__search_params.abtest = Abtest()
        self.__search_params.abtest.flowDivider = flow_divider

    def set_user_id(self, user_id):
        """设置终端用户的id，用来统计uv信息。
        :param user_id: 设定终端用户的id。
        """
        self.__search_params.userId = user_id

    def set_raw_query(self, raw_query):
        """设置终端用户输入的query。
        :param raw_query: 设定终端用户输入的query。
        """
        self.__search_params.rawQuery = raw_query
