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
    api = opensearch.DefaultApi(client)

    response = api.v3_openapi_apps_app_name_search_get(app_name, 'query=default:\'天猫\'')
    print(response)
