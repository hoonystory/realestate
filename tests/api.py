import webbrowser
from src.utils.url import URLQueryString

# Ak5ExMq7svgb45fKdmgOJOaWOOrp5KAa7LUiJ1fc7cRujpLh5bVWLtnfzd1ft0nuLT0nZiTv9T1u7vLoVw5Kzg==
# Ak5ExMq7svgb45fKdmgOJOaWOOrp5KAa7LUiJ1fc7cRujpLh5bVWLtnfzd1ft0nuLT0nZiTv9T1u7vLoVw5Kzg%3D%3D

api_access_key = 'Ak5ExMq7svgb45fKdmgOJOaWOOrp5KAa7LUiJ1fc7cRujpLh5bVWLtnfzd1ft0nuLT0nZiTv9T1u7vLoVw5Kzg=='

api_request_url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc'
svc_apt_trade_url = '/getRTMSDataSvcAptTrade'
svc_sht_trade_url = '/getRTMSDataSvcSHTrade'


def get_real_txn_apt_trade(LAWD_CD, DEAL_YMD, serviceKey):

    from_array = URLQueryString() \
        .set('LAWD_CD', LAWD_CD) \
        .set('DEAL_YMD', DEAL_YMD) \
        .set('serviceKey', serviceKey)
    # from_array.set('LAWD_CD', LAWD_CD)
    # from_array.set('DEAL_YMD', DEAL_YMD)
    # from_array.set('serviceKey', serviceKey)

    result_url = api_request_url + svc_apt_trade_url + from_array.get_query_string()
    print(result_url)

    webbrowser.open(result_url)
    return


get_real_txn_apt_trade('11110', '202001', api_access_key)
