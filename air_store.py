from matplotlib import pyplot
from pandas import Series


def plot_air_store(air_store_info):
    # plot_air_store_genres(air_store_info)
    plot_air_store_areas(air_store_info)


def plot_air_store_genres(air_store_info):
    air_genre_name: Series = air_store_info['air_genre_name']
    air_genre_name_counts: Series = air_genre_name.value_counts()

    ax = air_genre_name_counts.plot(kind='bar')
    ax.grid('on', which='major', axis='y', linestyle='-', linewidth=0.1)
    ax.set_title("Type of cuisine (air restaurants)")
    ax.set_ylabel("Number of air restaurants")

    pyplot.tight_layout()
    # pyplot.show()
    pyplot.savefig('figures/air_store_type_of_cuisine.png', dpi=300)


def plot_air_store_areas(air_store_info):

    air_area_name: Series = air_store_info['air_area_name']
    air_area_name_counts: Series = air_area_name.value_counts()

    ax = air_area_name_counts[0:14].plot(kind='bar')
    ax.grid('on', which='major', axis='y', linestyle='-', linewidth=0.1)
    ax.set_title("Areas (air restaurants)")
    ax.set_ylabel("Number of air restaurants")

    pyplot.tight_layout()
    # pyplot.show()
    pyplot.savefig('figures/air_store_areas.png', dpi=300)


def plot_hpg_store(hpg_store_info):
    # plot_hpg_store_genres(hpg_store_info)
    plot_hpg_store_areas(hpg_store_info)


def plot_hpg_store_genres(hpg_store_info):
    hpg_genre_name: Series = hpg_store_info['hpg_genre_name']
    hpg_genre_name_counts: Series = hpg_genre_name.value_counts()

    ax = hpg_genre_name_counts.plot(kind='bar')
    ax.grid('on', which='major', axis='y', linestyle='-', linewidth=0.1)
    ax.set_title("Type of cuisine (hpg restaurants)")
    ax.set_ylabel("Number of hpg restaurants")

    pyplot.tight_layout()
    # pyplot.show()
    pyplot.savefig('figures/hpg_store_type_of_cuisine.png', dpi=300)


def plot_hpg_store_areas(hpg_store_info):
    hpg_area_name: Series = hpg_store_info['hpg_area_name']
    hpg_area_name_counts: Series = hpg_area_name.value_counts()

    ax = hpg_area_name_counts[0:14].plot(kind='bar')
    ax.grid('on', which='major', axis='y', linestyle='-', linewidth=0.1)
    ax.set_title("Areas (hpg restaurants)")
    ax.set_ylabel("Number of hpg restaurants")

    pyplot.tight_layout()
    # pyplot.show()
    pyplot.savefig('figures/hpg_store_areas.png', dpi=300)

