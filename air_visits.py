from matplotlib import pyplot
import matplotlib.dates as mdates


def plot_all_visitors_by_date(air_visit_data):
    ax = air_visit_data.groupby('visit_date').sum().plot()
    ax.set_title("Total visitors per day")
    ax.set_xlabel('Date')
    ax.set_ylabel('All visitors per day')
    ax.set_xticklabels(air_visit_data.index, rotation=90)

    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))
    ax.grid('on', which='minor', axis='x', linestyle='-', linewidth=0.1)
    ax.grid('on', which='major', axis='y', linestyle='-', linewidth=0.1)

    pyplot.tight_layout()
    pyplot.show()
    pyplot.savefig('figures/all_visitors_by_date.png', dpi=300)

