import os
from pathlib import Path


def get_request_info(key):
    return api_info.get(key, '')


def get_data_result_column(key):
    return columns.get(key, [])


def get_project_root_path():
    return Path(__file__).parent.parent


def get_database_path():
    return os.path.join(get_project_root_path(), 'db')


def get_resource_path():
    return os.path.join(get_project_root_path(), 'resources')


api_info = {
    'access_key':
        'Ak5ExMq7svgb45fKdmgOJOaWOOrp5KAa7LUiJ1fc7cRujpLh5bVWLtnfzd1ft0nuLT0nZiTv9T1u7vLoVw5Kzg==',
    'request_url':
        'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc',
    'real_txn_apt_trade':
        '/getRTMSDataSvcAptTrade',
    'real_txn_sht_trade':
        '/getRTMSDataSvcSHTrade'
}

columns = {
    'real_txn_apt_trade': {
        'dealAmount': '거래금액'
        , 'buildYear': '건축년도'
        , 'dealYear': '년'
        , 'dong': '법정동'
        , 'apartment': '아파트'
        , 'dealMonth': '월'
        , 'dealDay': '일'
        , 'exclusiveArea': '전용면적'
        , 'jibun': '지번'
        , 'regionCode': '지역코드'
        , 'floor': '층'
    }
}