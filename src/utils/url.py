class URLQueryString:
    def __init__(self):
        self.querystring_array = []
        self.logging_array = []

    def set(self, key, value):
        '''
            set query string for request api. return for chaining method
            :param key
            :param value
            :return
        '''
        array_item = key + '=' + value
        self.querystring_array.append(array_item)
        if key != 'serviceKey':
            self.logging_array.append(array_item)
        return self

    def get_query_string(self):
        '''
            get query string for request api
            :return
        '''
        return '?' + '&'.join(self.querystring_array)

    def get_except_service_key(self):
        '''
            get query string when request api for logging
            :return
        '''
        return '?' + '&'.join(self.logging_array)