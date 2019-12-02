# coding: utf-8

import opensearch
import json

if __name__ == "__main__":
    app_name = "APP_NAME"

    config = opensearch.Configuration()
    config.host = "http://opensearch-cn-hangzhou.aliyuncs.com"
    config.access_key = "ACCESS_KEY"
    config.access_key_secret = "SECRET"

    client = opensearch.ApiClient(config)

    auth_settings = ['opensearch']
    response = client.call_api("/v3/openapi/app-groups/" + app_name,
        'GET', response_type="object", _return_http_data_only=True, auth_settings=auth_settings)
    print(response)
