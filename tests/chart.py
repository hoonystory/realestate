from src.utils import data_frame as from_instance
import matplotlib.pyplot as plt
from src.utils import db


# test select inserted data
sql = 'select dealAmount, dealDay' \
      ', (dealYear || "/" || dealMonth) as dealYear from real_txn_apt_trade'
db_instance = db.Sqlite3('data')
df = from_instance.get_data_frame_from_database(db_instance, sql)
print(df)

# test visualize data by using matplotlib
df_deal_amount = df['dealAmount']
print(df_deal_amount.describe())

data_dict = {
      'x': df['dealDay']
      , 'y': df['dealAmount']
}

# 선차트, 기본 차트
# plt.plot('x', 'y', data=data_dict)

# 산점도, 거래 금액에 대한 빈도수 표현
# plt.scatter(df['dealDay'], df['dealAmount'])

# 히스토그램, 거래 금액 빈도수 표현
# plt.hist(df['dealAmount'])
# plt.hist(df['dealAmount'], bins=30)
# plt.legend()

# 히스토그램, 거래일 빈도수 표현
plt.hist(df['dealDay'], bins=30)
plt.legend()

plt.show()
