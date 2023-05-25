def get_file_path(*args):
    result_array = []
    for i in args:
        result_array.append(i)
    return '/'.join(result_array)

