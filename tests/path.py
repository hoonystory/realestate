import os
from pathlib import Path
from src.model import table


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)
print(Path(__file__).parent.parent)

path_varibles = ( Path(__file__).parent.parent, 'db')
print(os.path.join(Path(__file__).parent.parent, 'db'))


for key, value in table.get_database_table_info('code', 'lawd_cd').items():
    print(key + ' ' + value)