from src.utils.log import logger


# test for using constant for dictionary key
# test_key = 'code'
# table = {
#     test_key: {
#         'lawd_cd': {
#             'lawd_cd': 'integer'
#             , 'dong_nm': 'text'
#             , 'exyn': 'text'
#         }
#     }
#     , 'test_database': {
#         'test_table': {
#             'test_column': 'integer'
#         }
#         , 'test_table_2': {
#             'test_column2': 'text'
#         }
#     }
# }
# print(table)


# test recursive find
def recursive_get(d, *args, default=None):
    if not args:
        return d
    key, *args = args
    return recursive_get(d.get(key, default), *args, default=default)


def iterdict(d, key):
    for k, v in d.items():
        if k == key:
            print(k, ":", v)
            return v
        if isinstance(v, dict):
            iterdict(v, key)

        # else:
        #     print(k, ":", v)


# print(table.get('test_table', {}))
# print(recursive_get(table, 'test_table'))
# iterdict(table, 'test_table')

table = {
    'code': {
        'lawd_cd': {
            'lawd_cd': 'integer'
            , 'dong_nm': 'text'
            , 'exyn': 'text'
        }
    },
    'data': {
        'real_txn_apt_trade': {
            'dealAmount': 'integer'
            , 'buildYear': 'integer'
            , 'dealYear': 'integer'
            , 'dong': 'text'
            , 'apartment': 'text'
            , 'dealMonth': 'integer'
            , 'dealDay': 'integer'
            , 'exclusiveArea': 'real'
            , 'jibun': 'text'
            , 'regionCode': 'integer'
            , 'floor': 'integer'
        }
    }
}

result = iterdict(table, 'lawd_cd')
print(result)


# array index test
need_to_parse_list = [ 'integer' , 'real' ]
print(need_to_parse_list.count('integer'))


# test logger
# logger.info('test')

# test parse string to float
# float_string = '194.43'
# converted_to_float = float(float_string)
# print(converted_to_float)
# print(type(converted_to_float))
