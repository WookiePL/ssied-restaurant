import pandas as pd
from matplotlib import pyplot

date_info = pd.read_csv("dane/date_info.csv")
air_reserve = pd.read_csv("dane/air_reserve.csv")
air_store_info = pd.read_csv("dane/air_store_info.csv")
air_visit_data = pd.read_csv("dane/air_visit_data.csv", index_col=1, parse_dates=[1])
hpg_reserve = pd.read_csv("dane/hpg_reserve.csv")
hpg_store_info = pd.read_csv("dane/hpg_store_info.csv")
sample_submission = pd.read_csv("dane/sample_submission.csv")
store_id_relation = pd.read_csv("dane/store_id_relation.csv")

print(air_visit_data)

air_visit_data['visitors'].plot()
pyplot.show()
