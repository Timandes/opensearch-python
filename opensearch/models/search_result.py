# coding: utf-8

"""
   Copyright 2019 Alibaba Group Holding Limited

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


import pprint
import re  # noqa: F401

import six

from opensearch.models.search_result_facet import SearchResultFacet  # noqa: F401,E501
from opensearch.models.search_result_item import SearchResultItem  # noqa: F401,E501


class SearchResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'searchtime': 'object',
        'total': 'int',
        'viewtotal': 'int',
        'num': 'int',
        'items': 'list[SearchResultItem]',
        'facet': 'list[SearchResultFacet]'
    }

    attribute_map = {
        'searchtime': 'searchtime',
        'total': 'total',
        'viewtotal': 'viewtotal',
        'num': 'num',
        'items': 'items',
        'facet': 'facet'
    }

    def __init__(self, searchtime=None, total=None, viewtotal=None, num=None, items=None, facet=None):  # noqa: E501
        """SearchResult - a model defined in Swagger"""  # noqa: E501

        self._searchtime = None
        self._total = None
        self._viewtotal = None
        self._num = None
        self._items = None
        self._facet = None
        self.discriminator = None

        if searchtime is not None:
            self.searchtime = searchtime
        if total is not None:
            self.total = total
        if viewtotal is not None:
            self.viewtotal = viewtotal
        if num is not None:
            self.num = num
        if items is not None:
            self.items = items
        if facet is not None:
            self.facet = facet

    @property
    def searchtime(self):
        """Gets the searchtime of this SearchResult.  # noqa: E501

        指引擎耗时，单位为秒。  # noqa: E501

        :return: The searchtime of this SearchResult.  # noqa: E501
        :rtype: object
        """
        return self._searchtime

    @searchtime.setter
    def searchtime(self, searchtime):
        """Sets the searchtime of this SearchResult.

        指引擎耗时，单位为秒。  # noqa: E501

        :param searchtime: The searchtime of this SearchResult.  # noqa: E501
        :type: object
        """

        self._searchtime = searchtime

    @property
    def total(self):
        """Gets the total of this SearchResult.  # noqa: E501

        total为一次查询（不考虑config子句）引擎中符合条件的结果数（在结果数较多情况下，该值会做优化），一般用来做展示。  # noqa: E501

        :return: The total of this SearchResult.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SearchResult.

        total为一次查询（不考虑config子句）引擎中符合条件的结果数（在结果数较多情况下，该值会做优化），一般用来做展示。  # noqa: E501

        :param total: The total of this SearchResult.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def viewtotal(self):
        """Gets the viewtotal of this SearchResult.  # noqa: E501

        考虑到性能及相关性，引擎最多会返回viewtotal个结果。如果需要翻页的话，要求start+hit必需要小于viewtotal  # noqa: E501

        :return: The viewtotal of this SearchResult.  # noqa: E501
        :rtype: int
        """
        return self._viewtotal

    @viewtotal.setter
    def viewtotal(self, viewtotal):
        """Sets the viewtotal of this SearchResult.

        考虑到性能及相关性，引擎最多会返回viewtotal个结果。如果需要翻页的话，要求start+hit必需要小于viewtotal  # noqa: E501

        :param viewtotal: The viewtotal of this SearchResult.  # noqa: E501
        :type: int
        """

        self._viewtotal = viewtotal

    @property
    def num(self):
        """Gets the num of this SearchResult.  # noqa: E501

        num为本次查询请求（受限于config子句的start及hit）实际返回的条目，不会超过hit值。  # noqa: E501

        :return: The num of this SearchResult.  # noqa: E501
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this SearchResult.

        num为本次查询请求（受限于config子句的start及hit）实际返回的条目，不会超过hit值。  # noqa: E501

        :param num: The num of this SearchResult.  # noqa: E501
        :type: int
        """

        self._num = num

    @property
    def items(self):
        """Gets the items of this SearchResult.  # noqa: E501

        包含查询召回数据信息，其中fields为搜索召回内容。  # noqa: E501

        :return: The items of this SearchResult.  # noqa: E501
        :rtype: list[SearchResultItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this SearchResult.

        包含查询召回数据信息，其中fields为搜索召回内容。  # noqa: E501

        :param items: The items of this SearchResult.  # noqa: E501
        :type: list[SearchResultItem]
        """

        self._items = items

    @property
    def facet(self):
        """Gets the facet of this SearchResult.  # noqa: E501

        用于存放Aggregate子句返回的信息。  # noqa: E501

        :return: The facet of this SearchResult.  # noqa: E501
        :rtype: list[SearchResultFacet]
        """
        return self._facet

    @facet.setter
    def facet(self, facet):
        """Sets the facet of this SearchResult.

        用于存放Aggregate子句返回的信息。  # noqa: E501

        :param facet: The facet of this SearchResult.  # noqa: E501
        :type: list[SearchResultFacet]
        """

        self._facet = facet

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SearchResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
