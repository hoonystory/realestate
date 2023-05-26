import os
from pathlib import Path
from src.model import table as from_table


# find the project root path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)
print(Path(__file__).parent.parent)

# concatenate absolute path with file path
path_variables = (Path(__file__).parent.parent, 'db')
print(os.path.join(Path(__file__).parent.parent, 'db'))


for key, value in table.get_table_info_from_database('code', 'lawd_cd').items():
    print(key + ' ' + value)
