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


def plot_reservation_hours(reserve, prefix):
    reserve['visit_datetime'] = reserve['visit_datetime'].dt.time

    ts = reserve.groupby('visit_datetime')['reserve_visitors'].sum()
    ax = ts.plot(kind='bar')
    ax.set_xlabel("Date")
    ax.set_ylabel("All visitors")
    for tick in ax.get_xticklabels():
        tick.set_rotation(90)

    for bar in ax.patches:
        bar.set_facecolor('#0000ff')

    ax.grid('on', which='minor', axis='x', linestyle='-', linewidth=0.1)
    ax.grid('on', which='major', axis='y', linestyle='-', linewidth=0.1)
    ax.axhline(y=ts.mean().item(), color='r', linestyle='--', lw=0.5)
    ax.legend(['Mean visitors count per hour','Visitors'])

    pyplot.tight_layout()
    # pyplot.show()
    pyplot.savefig('figures/' + prefix + '_reservation_hours.png', dpi=300)


def plot_time_from_reservation_to_visit(reserve, prefix):
    reserve['Difference'] = reserve['visit_datetime'].sub(reserve['reserve_datetime'], axis=0)
    tmp = reserve[['Difference', 'reserve_visitors']]
    print(tmp)

    ts = tmp.groupby('Difference')['reserve_visitors'].sum().plot(kind='bar')
    ts.set_xlim(-10, 400)

    for bar in ts.patches:
        bar.set_facecolor('#0000ff')

    pyplot.tight_layout()
    pyplot.show()
    # trzeba tutaj jakoś wyświetlić co 20 labelkę