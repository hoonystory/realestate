import webbrowser

# Ak5ExMq7svgb45fKdmgOJOaWOOrp5KAa7LUiJ1fc7cRujpLh5bVWLtnfzd1ft0nuLT0nZiTv9T1u7vLoVw5Kzg==
# Ak5ExMq7svgb45fKdmgOJOaWOOrp5KAa7LUiJ1fc7cRujpLh5bVWLtnfzd1ft0nuLT0nZiTv9T1u7vLoVw5Kzg%3D%3D
api_access_key = 'Ak5ExMq7svgb45fKdmgOJOaWOOrp5KAa7LUiJ1fc7cRujpLh5bVWLtnfzd1ft0nuLT0nZiTv9T1u7vLoVw5Kzg=='

api_request_url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc'
svc_apt_trade_url = '/getRTMSDataSvcAptTrade'
svc_sht_trade_url = '/getRTMSDataSvcSHTrade'


class request:
    def __init__(self):
        self.querystring_array = []

    def set(self, key, value):
        self.querystring_array.append(key + '=' + value)

    def get(self):
        return '?' + '&'.join(self.querystring_array)


def getRTMSDataSvcAptTrade(LAWD_CD, DEAL_YMD, serviceKey):
    result = request()
    result.set('LAWD_CD', LAWD_CD)
    result.set('DEAL_YMD', DEAL_YMD)
    result.set('serviceKey', serviceKey)

    result_url = api_request_url + svc_apt_trade_url + result.get()
    print(result_url)

    webbrowser.open(result_url)
    return


getRTMSDataSvcAptTrade('11110', '202001', api_access_key)
