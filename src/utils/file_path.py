import os.path
from pathlib import Path


def get_file_path(*args):
    result_array = []
    for i in args:
        result_array.append(i)
    return '/'.join(result_array)


def is_file_exists(file_path):
    return os.path.exists(file_path)


def get_project_root_path():
    # Path(__file__).parent.parent
    return '/Users/hoony/IdeaProjects/realestate'


def get_database_path():
    return os.path.join(get_project_root_path(), 'db')


def get_resource_path():
    return os.path.join(get_project_root_path(), 'resources')