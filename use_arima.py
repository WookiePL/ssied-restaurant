import statsmodels.api as sm
from matplotlib import pyplot


def predict_arima(time_series, start_index, stop_index):
    mod = sm.tsa.statespace.SARIMAX(time_series.visitors, trend='n', order=(1, 1, 1), seasonal_order=(1, 1, 1, 52))
    results = mod.fit()
    print(results.summary())
    time_series['forecast'] = results.predict(start=start_index, end=stop_index, dynamic=True)
    time_series[['visitors', 'forecast']][start_index:stop_index].plot(figsize=(12, 8))
    pyplot.show()

