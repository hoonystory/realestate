from src.utils import db


def test_args(*args):
    print('length of tuple: ' + str(len(args)))
    if len(args) != 0:
        empty_arg = args[0]
        print('first_argument: ' + empty_arg)


# test for what will be happening when there's no parameter in function
test_args()

# what will happen when empty string, nothing in parameter.
#   - .db file created, surprisingly
sql = 'select count(*) from sqlite_master'
db_instance = db.Sqlite3()
db_instance.cursor.execute(sql)
result = db_instance.cursor.fetchall()
print(result)
print(db_instance.db_path)
