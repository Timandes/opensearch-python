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

import base64
import hmac
import random
import time
import urllib
from hashlib import sha1


def sign_for_v3(uri, params, request_headers, access_key, access_secret, method="GET"):
    request_headers["Date"] = _generate_date()
    request_headers["X-Opensearch-Nonce"] = _generate_nonce()
    canonicalized = _build_sign_str(uri, request_headers, params, method)
    h = hmac.new(access_secret, canonicalized, sha1)
    sign = base64.encodestring(h.digest()).strip()
    return "OPENSEARCH %s:%s" % (access_key, sign)


def _generate_date(date_format="%Y-%m-%dT%H:%M:%SZ", timestamp=None):
    if timestamp is None:
        return time.strftime(date_format, time.gmtime())
    else:
        return time.strftime(date_format, timestamp)


def _generate_nonce():
    return str(int(time.time() * 100)) + str(random.randint(10000, 99999))


def _build_sign_str(uri, request_headers, params, method="GET"):
    return method + "\n" \
           + _get_header(request_headers, "Content-MD5", "") + "\n" \
           + _get_header(request_headers, "Content-Type", "") + "\n" \
           + request_headers["Date"] + "\n" \
           + _canonicalized_headers(request_headers) \
           + _canonicalized_source(uri, params)


def _canonicalized_source(uri, params):
    canonicalized = urllib.quote(uri).replace("%2F", "/").replace("%3F", "?").replace("%3D", "=").replace("%26", "&")
    sorted_params = sorted(params.items(), key=lambda http_params: http_params[0])
    params_to_sign = []
    for (key, value) in sorted_params:
        if value is None or len(value) == 0:
            continue
        params_to_sign.append(urllib.quote(key) + "=" + urllib.quote(value))
    if len(params_to_sign) > 0:
        return canonicalized + "?" + "&".join(params_to_sign)
    return canonicalized


def _get_header(header, key, default_value=None):
    if key in header and header[key] is not None:
        return header[key]
    return default_value


def _canonicalized_headers(request_headers):
    header = {}
    for key, value in request_headers.iteritems():
        if key is None or value is None:
            continue
        k = key.strip(" \t")
        v = value.strip(" \t")
        if k.startswith("X-Opensearch-") and len(v) > 0:
            header[k] = v

    if len(header) == 0:
        return ""

    sorted_header = sorted(header.items(), key=lambda header: header[0])
    canonicalized = ""
    for (key, value) in sorted_header:
        canonicalized += (key.lower() + ":" + value + "\n")
    return canonicalized
