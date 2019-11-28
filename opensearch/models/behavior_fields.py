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


class BehaviorFields(object):
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
        'event_id': 'int',
        'sdk_type': 'str',
        'sdk_version': 'str',
        'page': 'str',
        'arg1': 'str',
        'arg3': 'str',
        'args': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'event_id': 'event_id',
        'sdk_type': 'sdk_type',
        'sdk_version': 'sdk_version',
        'page': 'page',
        'arg1': 'arg1',
        'arg3': 'arg3',
        'args': 'args',
        'user_id': 'user_id'
    }

    def __init__(self, event_id=None, sdk_type=None, sdk_version=None, page=None, arg1=None, arg3=None, args=None, user_id=None):  # noqa: E501
        """BehaviorFields - a model defined in Swagger"""  # noqa: E501

        self._event_id = None
        self._sdk_type = None
        self._sdk_version = None
        self._page = None
        self._arg1 = None
        self._arg3 = None
        self._args = None
        self._user_id = None
        self.discriminator = None

        self.event_id = event_id
        self.sdk_type = sdk_type
        self.sdk_version = sdk_version
        self.page = page
        if arg1 is not None:
            self.arg1 = arg1
        if arg3 is not None:
            self.arg3 = arg3
        if args is not None:
            self.args = args
        if user_id is not None:
            self.user_id = user_id

    @property
    def event_id(self):
        """Gets the event_id of this BehaviorFields.  # noqa: E501

        埋点的事件ID，详见埋点规范，不能为空  # noqa: E501

        :return: The event_id of this BehaviorFields.  # noqa: E501
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this BehaviorFields.

        埋点的事件ID，详见埋点规范，不能为空  # noqa: E501

        :param event_id: The event_id of this BehaviorFields.  # noqa: E501
        :type: int
        """
        if event_id is None:
            raise ValueError("Invalid value for `event_id`, must not be `None`")  # noqa: E501

        self._event_id = event_id

    @property
    def sdk_type(self):
        """Gets the sdk_type of this BehaviorFields.  # noqa: E501

        sdk类型， 如果使用sdk上传则为'opensearch_sdk'，不能为空  # noqa: E501

        :return: The sdk_type of this BehaviorFields.  # noqa: E501
        :rtype: str
        """
        return self._sdk_type

    @sdk_type.setter
    def sdk_type(self, sdk_type):
        """Sets the sdk_type of this BehaviorFields.

        sdk类型， 如果使用sdk上传则为'opensearch_sdk'，不能为空  # noqa: E501

        :param sdk_type: The sdk_type of this BehaviorFields.  # noqa: E501
        :type: str
        """
        if sdk_type is None:
            raise ValueError("Invalid value for `sdk_type`, must not be `None`")  # noqa: E501

        self._sdk_type = sdk_type

    @property
    def sdk_version(self):
        """Gets the sdk_version of this BehaviorFields.  # noqa: E501

        opensearch_sdk版本号，不能为空  # noqa: E501

        :return: The sdk_version of this BehaviorFields.  # noqa: E501
        :rtype: str
        """
        return self._sdk_version

    @sdk_version.setter
    def sdk_version(self, sdk_version):
        """Sets the sdk_version of this BehaviorFields.

        opensearch_sdk版本号，不能为空  # noqa: E501

        :param sdk_version: The sdk_version of this BehaviorFields.  # noqa: E501
        :type: str
        """
        if sdk_version is None:
            raise ValueError("Invalid value for `sdk_version`, must not be `None`")  # noqa: E501

        self._sdk_version = sdk_version

    @property
    def page(self):
        """Gets the page of this BehaviorFields.  # noqa: E501

        当前页面，不能为空  # noqa: E501

        :return: The page of this BehaviorFields.  # noqa: E501
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this BehaviorFields.

        当前页面，不能为空  # noqa: E501

        :param page: The page of this BehaviorFields.  # noqa: E501
        :type: str
        """
        if page is None:
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    @property
    def arg1(self):
        """Gets the arg1 of this BehaviorFields.  # noqa: E501

        事件参数，默认为空。当事件为2001时该参数代表搜索结果列表所在的页面名称，不能为空  # noqa: E501

        :return: The arg1 of this BehaviorFields.  # noqa: E501
        :rtype: str
        """
        return self._arg1

    @arg1.setter
    def arg1(self, arg1):
        """Sets the arg1 of this BehaviorFields.

        事件参数，默认为空。当事件为2001时该参数代表搜索结果列表所在的页面名称，不能为空  # noqa: E501

        :param arg1: The arg1 of this BehaviorFields.  # noqa: E501
        :type: str
        """

        self._arg1 = arg1

    @property
    def arg3(self):
        """Gets the arg3 of this BehaviorFields.  # noqa: E501

        事件参数，默认为空。当事件为2001时该参数代表用户在详情页停留的时长（单位ms），不能为空  # noqa: E501

        :return: The arg3 of this BehaviorFields.  # noqa: E501
        :rtype: str
        """
        return self._arg3

    @arg3.setter
    def arg3(self, arg3):
        """Sets the arg3 of this BehaviorFields.

        事件参数，默认为空。当事件为2001时该参数代表用户在详情页停留的时长（单位ms），不能为空  # noqa: E501

        :param arg3: The arg3 of this BehaviorFields.  # noqa: E501
        :type: str
        """

        self._arg3 = arg3

    @property
    def args(self):
        """Gets the args of this BehaviorFields.  # noqa: E501

        事件参数，默认为空。当事件为2001时该参数为Event2001Args实体的字符串表示，不能为空  # noqa: E501

        :return: The args of this BehaviorFields.  # noqa: E501
        :rtype: str
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this BehaviorFields.

        事件参数，默认为空。当事件为2001时该参数为Event2001Args实体的字符串表示，不能为空  # noqa: E501

        :param args: The args of this BehaviorFields.  # noqa: E501
        :type: str
        """

        self._args = args

    @property
    def user_id(self):
        """Gets the user_id of this BehaviorFields.  # noqa: E501

        默认为空，实际中建议非空。该值可以设置为下列值，优先级从高到低：1. 终端用户的长登录会员ID；2. 终端用户的移动设备imei标识；3. 终端用户的client_ip  # noqa: E501

        :return: The user_id of this BehaviorFields.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BehaviorFields.

        默认为空，实际中建议非空。该值可以设置为下列值，优先级从高到低：1. 终端用户的长登录会员ID；2. 终端用户的移动设备imei标识；3. 终端用户的client_ip  # noqa: E501

        :param user_id: The user_id of this BehaviorFields.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(BehaviorFields, dict):
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
        if not isinstance(other, BehaviorFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other