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

from setuptools import setup, find_packages  # noqa: H301
from os.path import join, dirname

f = open(join(dirname(__file__), "README.md"))
long_description = f.read().strip()
f.close()

NAME = "opensearch"
VERSION = "0.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]


setup(
    name=NAME,
    version=VERSION,
    description="Python Client for Aliyun Opensearch",
    license="Apache License, Version 2.0",
    author="Timandes White",
    author_email="timands@gmail.com",
    url="https://github.com/timandes/opensearch-python",
    keywords=["Swagger", "Opensearch"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description
)
