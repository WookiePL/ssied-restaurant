import pandas as pd
from matplotlib import pyplot
import numpy as np
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm

import reservation
import air_visits
import air_store
from series_util import test_stationarity, difference, log
from use_arima import predict_arima

date_info = pd.read_csv("dane/date_info.csv")
air_reserve = pd.read_csv("dane/air_reserve.csv", index_col=2, parse_dates=[1, 2])
air_store_info = pd.read_csv("dane/air_store_info.csv")
air_visit_data = pd.read_csv("dane/air_visit_data.csv", index_col=1, parse_dates=[1])
hpg_reserve = pd.read_csv("dane/hpg_reserve.csv", index_col=2, parse_dates=[1, 2])
hpg_store_info = pd.read_csv("dane/hpg_store_info.csv")
sample_submission = pd.read_csv("dane/sample_submission.csv")
store_id_relation = pd.read_csv("dane/store_id_relation.csv")

# air_visits.plot_all_visitors_by_date(air_visit_data)

# air_reserve['visit_datetime'] = air_reserve['visit_datetime'].dt.date
# print(air_reserve.groupby('visit_datetime')['reserve_visitors'].sum())


#air_visits.plot_all_visitors_by_date(air_visit_data)
#air_visits.plot_visitors_by_month(air_visit_data)
#air_visits.plot_visitors_by_day_of_week(air_visit_data)

reservation.plot_reservation(air_reserve, 'air')
reservation.plot_reservation(hpg_reserve, 'hpg')


# print(hpg_reserve)
#air_visit_data['visitors'].plot()
#pyplot.show()

# air_store.plot_air_store(air_store_info)
# air_store.plot_hpg_store(hpg_store_info)


def arima_example():
    filtered = air_visit_data.loc[air_visit_data['air_store_id'] == 'air_789466e488705c93']
    print(filtered['visitors'].head)
    df = filtered
    # pre-processing
    df['log'] = log(series=df['visitors'])
    df['log_seasonal_diff'] = difference(series=df['visitors'], shift_value=7)
    # run dickey-fuller test
    test_stationarity(df['log_seasonal_diff'].dropna(inplace=False))
    # calculate predictions
    start = df.index.get_loc('20170401')
    stop = df.index.get_loc('20170422')
    predict_arima(df, start, stop)
