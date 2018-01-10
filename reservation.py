from matplotlib import pyplot


def plot_reservation(reserve, prefix):
    reserve['visit_datetime'] = reserve['visit_datetime'].dt.date

    ts = reserve.groupby('visit_datetime')['reserve_visitors'].sum()
    ax = ts.plot()
    ax.set_xlabel("Date")
    ax.set_ylabel("All visitors")
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)

    ax.grid('on', which='minor', axis='x', linestyle='-', linewidth=0.1)
    ax.grid('on', which='major', axis='y', linestyle='-', linewidth=0.1)
    ax.axhline(y=ts.mean().item(), color='r', linestyle='--', lw=0.5)
    ax.legend(['Visitors', 'Mean visitors count per day'])

    pyplot.tight_layout()
    # pyplot.show()
    pyplot.savefig('figures/' + prefix + '_reservation.png', dpi=300)
