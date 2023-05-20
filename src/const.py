# Decorator
def constant(func):
    def func_set(self, value):
        raise TypeError

    def func_get(self):
        return func()

    return property(func_get, func_set)


# const class
# noinspection PyMethodParameters
class Const(object):
    # instance = None
    #
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(Const, cls).__new__(cls)
    #     else:
    #         return cls.instance

    @constant
    def api_access_key():
        return 'Ak5ExMq7svgb45fKdmgOJOaWOOrp5KAa7LUiJ1fc7cRujpLh5bVWLtnfzd1ft0nuLT0nZiTv9T1u7vLoVw5Kzg=='

    @constant
    def api_request_url():
        return 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc'

    @constant
    def svc_apt_trade_url():
        return '/getRTMSDataSvcAptTrade'

    @constant
    def svc_sht_trade_url():
        return '/getRTMSDataSvcSHTrade'


const = Const()
