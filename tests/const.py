# Decorator
def constant(func):
    def func_set(self, value):
        raise TypeError

    def func_get(self):
        return func()

    return property(func_get, func_set)


# const class
# noinspection PyMethodParameters
class _Const(object):
    @constant
    def api_access_key():
        return ''

    @constant
    def api_request_url():
        return 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc'

    @constant
    def svc_apt_trade_url():
        return '/getRTMSDataSvcAptTrade'

    @constant
    def svc_sht_trade_url():
        return '/getRTMSDataSvcSHTrade'


CONST = _Const()
print(CONST.api_access_key)