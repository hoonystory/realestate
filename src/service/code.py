from src.utils import db


def get_lawd_cd_list(region):
    db_instance = db.Sqlite3('code')

    # todo: separate code based on region
    #   - select distinct substr(lawd_cd, 0, 6) as lawd_cd from lawd_cd where lawd_cd like '11%'
    #   - select count(distinct substr(lawd_cd, 0, 6)) from lawd_cd where lawd_cd like '11%'

    sql = 'select distinct substr(lawd_cd, 0, 6) as lawd_cd ' \
          'from lawd_cd ' \
          'where lawd_cd like \'11%\''
