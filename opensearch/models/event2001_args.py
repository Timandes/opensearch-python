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


class Event2001Args(object):
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
        'object_id': 'str',
        'object_type': 'str',
        'ops_request_misc': 'str'
    }

    attribute_map = {
        'object_id': 'object_id',
        'object_type': 'object_type',
        'ops_request_misc': 'ops_request_misc'
    }

    def __init__(self, object_id=None, object_type='ops_search_doc', ops_request_misc=None):  # noqa: E501
        """Event2001Args - a model defined in Swagger"""  # noqa: E501

        self._object_id = None
        self._object_type = None
        self._ops_request_misc = None
        self.discriminator = None

        if object_id is not None:
            self.object_id = object_id
        if object_type is not None:
            self.object_type = object_type
        if ops_request_misc is not None:
            self.ops_request_misc = ops_request_misc

    @property
    def object_id(self):
        """Gets the object_id of this Event2001Args.  # noqa: E501

        被点击的对象的主键，不能为空，如果通过api上传需要urlencode  # noqa: E501

        :return: The object_id of this Event2001Args.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this Event2001Args.

        被点击的对象的主键，不能为空，如果通过api上传需要urlencode  # noqa: E501

        :param object_id: The object_id of this Event2001Args.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def object_type(self):
        """Gets the object_type of this Event2001Args.  # noqa: E501

        必须为ops_search_doc  # noqa: E501

        :return: The object_type of this Event2001Args.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this Event2001Args.

        必须为ops_search_doc  # noqa: E501

        :param object_type: The object_type of this Event2001Args.  # noqa: E501
        :type: str
        """

        self._object_type = object_type

    @property
    def ops_request_misc(self):
        """Gets the ops_request_misc of this Event2001Args.  # noqa: E501

        开放搜索在搜索结果中返回的参数，只要原样设置即可。  # noqa: E501

        :return: The ops_request_misc of this Event2001Args.  # noqa: E501
        :rtype: str
        """
        return self._ops_request_misc

    @ops_request_misc.setter
    def ops_request_misc(self, ops_request_misc):
        """Sets the ops_request_misc of this Event2001Args.

        开放搜索在搜索结果中返回的参数，只要原样设置即可。  # noqa: E501

        :param ops_request_misc: The ops_request_misc of this Event2001Args.  # noqa: E501
        :type: str
        """

        self._ops_request_misc = ops_request_misc

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
        if issubclass(Event2001Args, dict):
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
        if not isinstance(other, Event2001Args):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
