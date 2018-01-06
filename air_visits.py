import pandas as pd
from matplotlib import pyplot


def plot_all_visitors_by_date(air_visit_data):
    ax = air_visit_data.groupby('visit_date').sum().plot()
    ax.set_xlabel("Date")
    ax.set_ylabel("All visitors per day");
    pyplot.show()
