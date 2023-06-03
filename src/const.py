from src.utils import file_path


def get_access_key():
    root_path = file_path.get_project_root_path()
    f = open(root_path + '/resources/private/accessKey', 'r')
    access_key = f.readline()
    f.close()
    return access_key


def get_request_info(key):
    return api_info.get(key, '')


access_key = get_access_key()
api_info = {
    'access_key': access_key,
    'request_url': 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc',
    'real_txn_apt_trade': '/getRTMSDataSvcAptTrade',
    'real_txn_sht_trade': '/getRTMSDataSvcSHTrade'
}
