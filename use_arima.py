import statsmodels.api as sm
import pandas as pd
from dateutil.relativedelta import relativedelta
from matplotlib import pyplot
import matplotlib.dates as mdates
import matplotlib.ticker as mticker


@mticker.FuncFormatter
def month_formatter(x, pos):
    return pd.to_datetime(x, unit='D').strftime('%d-%m-%Y')

#seasonal_order=(3, 1, 1, 52))
def predict_arima(time_series, start_index, stop_index):
    mod = sm.tsa.statespace.SARIMAX(time_series['visitors'],  trend='n', order=(1, 0, 0), seasonal_order=(1, 1, 1, 52))
    results = mod.fit()
    print(results.summary())
    time_series['forecast'] = results.predict(start=start_index, end=stop_index, dynamic=True)

    air_id = time_series.iloc[1]['air_store_id']

    ax = time_series[['visitors', 'forecast']][start_index - 10:stop_index].plot(figsize=(12, 8))
    ax.set_title("Forecasting for air_id: " + air_id)
    ax.set_xlabel('Date')
    ax.set_ylabel('All visitors per day')

    # pyplot.tight_layout()
    pyplot.savefig('figures/predict/arima/'+str(air_id)+'.png', dpi=300)
    # pyplot.show()

    time_series['visitors'][start_index:stop_index + 1] = time_series['forecast'][start_index:stop_index + 1]
    return time_series


def arima_main(air_visit):
    # read input data
    air_visit = pd.read_csv("dane/air_visit_data.csv", index_col=1, parse_dates=[1])

    # Date range used for forecasting
    max_date = pd.to_datetime('20170531') # 2017-05-31
    min_date = pd.to_datetime('20170423') # 2017-04-23

    # Iterate through all restaurant ids
    air_ids = air_visit['air_store_id'].unique()
    for air in air_ids:
        air_restaurant = air_visit.loc[air_visit['air_store_id'] == air]

        # air_restaurant = air_visit_data.loc[air_visit_data['air_store_id'] == 'air_789466e488705c93']

        # cast data to float
        air_restaurant.visitors = air_restaurant.visitors.astype(float)

        # count how many days should added be to existing DataFrame to prepare it for forecasting
        last_date = air_restaurant.iloc[-1].name
        diff_days = (max_date - last_date).days
        date_list = [last_date + pd.DateOffset(1) + relativedelta(days=x) for x in range(0, diff_days)]
        future = pd.DataFrame(index=date_list, columns=air_restaurant.columns)
        # air store id = id
        future['air_store_id']=air
        # add missing rows
        air_restaurant = pd.concat([air_restaurant, future])

        # count start and stop indexes
        start = air_restaurant.index.get_loc(last_date)
        stop = start+diff_days

        # start forecasting
        air_restaurant = predict_arima(air_restaurant, start, stop)

        # extract result data
        predicted = air_restaurant[['visitors', 'air_store_id']][min_date:max_date]

        # cast visitors data to int
        predicted.visitors = predicted.visitors.astype(int)
        predicted['id'] = predicted.air_store_id + "_" + pd.to_datetime(predicted.index.date).strftime('%Y-%m-%d')
        # print(predicted.head)

        # save data in correct format
        predicted[['id', 'visitors']].to_csv('dane/submission.csv', mode='a', sep=',', encoding='utf-8', header=False,
                                             index=False)

