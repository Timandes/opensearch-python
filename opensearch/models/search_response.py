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

from opensearch.models.errors import Errors  # noqa: F401,E501
from opensearch.models.request_id import RequestId  # noqa: F401,E501
from opensearch.models.search_result import SearchResult  # noqa: F401,E501
from opensearch.models.status import Status  # noqa: F401,E501


class SearchResponse(object):
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
        'status': 'Status',
        'request_id': 'RequestId',
        'result': 'SearchResult',
        'errors': 'Errors'
    }

    attribute_map = {
        'status': 'status',
        'request_id': 'request_id',
        'result': 'result',
        'errors': 'errors'
    }

    def __init__(self, status=None, request_id=None, result=None, errors=None):  # noqa: E501
        """SearchResponse - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._request_id = None
        self._result = None
        self._errors = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if request_id is not None:
            self.request_id = request_id
        if result is not None:
            self.result = result
        if errors is not None:
            self.errors = errors

    @property
    def status(self):
        """Gets the status of this SearchResponse.  # noqa: E501


        :return: The status of this SearchResponse.  # noqa: E501
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SearchResponse.


        :param status: The status of this SearchResponse.  # noqa: E501
        :type: Status
        """

        self._status = status

    @property
    def request_id(self):
        """Gets the request_id of this SearchResponse.  # noqa: E501


        :return: The request_id of this SearchResponse.  # noqa: E501
        :rtype: RequestId
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this SearchResponse.


        :param request_id: The request_id of this SearchResponse.  # noqa: E501
        :type: RequestId
        """

        self._request_id = request_id

    @property
    def result(self):
        """Gets the result of this SearchResponse.  # noqa: E501


        :return: The result of this SearchResponse.  # noqa: E501
        :rtype: SearchResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this SearchResponse.


        :param result: The result of this SearchResponse.  # noqa: E501
        :type: SearchResult
        """

        self._result = result

    @property
    def errors(self):
        """Gets the errors of this SearchResponse.  # noqa: E501


        :return: The errors of this SearchResponse.  # noqa: E501
        :rtype: Errors
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this SearchResponse.


        :param errors: The errors of this SearchResponse.  # noqa: E501
        :type: Errors
        """

        self._errors = errors

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
        if issubclass(SearchResponse, dict):
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
        if not isinstance(other, SearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other