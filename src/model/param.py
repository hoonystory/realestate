from src.model import table


class Parameter:
    def __init__(self, tbl, *args):
        self.dict = {}
        self.table_nm = tbl
        request_param_key = table.get_table_request_params(tbl)
        if request_param_key:
            for i in range(request_param_key):
                self.dict[request_param_key[i].upper()] = args[i]

    # def set_request_param:
