class List:

    def __init__(self):
        self.key = ''
        self.result_list = []

    def set_key(self, key):
        self.key = key
        return self

    def set_result_list(self, result_list):
        self.result_list = result_list
        return self

    def get_key(self):
        return self.key

    def get_result_list(self):
        return self.result_list
