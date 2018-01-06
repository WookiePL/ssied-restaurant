from matplotlib import pyplot
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import pandas as pd


@mticker.FuncFormatter
def month_formatter(x, pos):
    return pd.to_datetime(x, unit='D').strftime('%b-%Y')


def plot_all_visitors_by_date(air_visit_data):
    ts = air_visit_data.groupby('visit_date').sum()
    ax = ts.plot()
    ax.set_title("Total visitors per day")
    ax.set_xlabel('Date')
    ax.set_ylabel('All visitors per day')
    ax.set_xticklabels(air_visit_data.index, rotation=90)

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(month_formatter)
    ax.grid('on', which='minor', axis='x', linestyle='-', linewidth=0.1)
    ax.grid('on', which='major', axis='y', linestyle='-', linewidth=0.1)
    ax.axhline(y = ts.mean().item(), color='r', linestyle='--', lw=0.5)
    ax.legend(['Visitors', 'Mean visitors per day'])

    pyplot.tight_layout()
    #pyplot.show()
    pyplot.savefig('figures/all_visitors_by_date.png', dpi=300)


def plot_visitors_by_day_of_week(air_visit_data):
    air_visit_data['day_of_week'] = pd.to_datetime(air_visit_data.index)
    grouped_by_dow = air_visit_data.groupby(air_visit_data['day_of_week'].dt.strftime('(%w) %a'))['visitors']
    dow_median = grouped_by_dow.median()
    dow_mean = grouped_by_dow.mean()

    ax = dow_median.plot(kind='bar')
    ax.set_title("Median visitors per day of week")
    ax.set_xlabel('Day of week')
    ax.set_ylabel('Median of visitors')
    ax.yaxis.set_major_locator(mticker.MultipleLocator(base=2.0))
    ax.grid('on', which='major', axis='y', linestyle='-', linewidth=0.1)
    pyplot.tight_layout()
    #pyplot.show()
    pyplot.savefig('figures/visitors_median_dayofweek.png', dpi=300)

    ax = dow_mean.plot(kind='bar')
    ax.set_title("Mean visitors per day of week")
    ax.set_xlabel('Day of week')
    ax.set_ylabel('Mean of visitors')
    ax.yaxis.set_major_locator(mticker.MultipleLocator(base=2.0))
    ax.grid('on', which='major', axis='y', linestyle='-', linewidth=0.1)
    pyplot.tight_layout()
    #pyplot.show()
    pyplot.savefig('figures/visitors_mean_dayofweek.png', dpi=300)


def plot_visitors_by_month(air_visit_data):

    air_visit_data['month'] = pd.to_datetime(air_visit_data.index)
    grouped_by_month = air_visit_data.groupby(air_visit_data['month'].dt.strftime('(%m) %b'))['visitors']
    month_median = grouped_by_month.median()
    month_mean = grouped_by_month.mean()

    ax = month_median.plot(kind='bar')
    ax.set_title("Median visitors per month")
    ax.set_xlabel('Month')
    ax.set_ylabel('Median of visitors')
    ax.yaxis.set_major_locator(mticker.MultipleLocator(base=2.0))
    ax.grid('on', which='major', axis='y', linestyle='-', linewidth=0.1)
    pyplot.tight_layout()
    #pyplot.show()
    pyplot.savefig('figures/visitors_median_month.png', dpi=300)

    ax = month_mean.plot(kind='bar')
    ax.set_title("Mean visitors per month")
    ax.set_xlabel('Month')
    ax.set_ylabel('Mean of visitors')
    ax.yaxis.set_major_locator(mticker.MultipleLocator(base=2.0))
    ax.grid('on', which='major', axis='y', linestyle='-', linewidth=0.1)
    pyplot.tight_layout()
    #pyplot.show()
    pyplot.savefig('figures/visitors_mean_month.png', dpi=300)