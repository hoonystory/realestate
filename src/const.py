def get_request_info(key):
    return api_info.get(key, '')


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
