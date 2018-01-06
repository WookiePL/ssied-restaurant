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

