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
    api = opensearch.DocumentClient(client)

    document = [{
        "cmd": "ADD",
        "fields": {
            "id": 123456,
            "name": "123456"
        }
    }]
    document_json = json.dumps(document)

    table_name = "categories"

    response = api.push(document_json, app_name, table_name)
    print(response)

    response = api.v3_openapi_apps_app_name_table_name_actions_bulk_post(app_name, table_name, document=document)
    print(response)
