import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from .analysis import polyfit

# for Task 2F

def plot_water_level_with_fit(station, dates, levels, p):

    low = []
    high = []
    for i in range(30):
        low.append(station.typical_range[0])
        high.append(station.typical_range[1])
        i += 1

    poly, d0 = polyfit(dates, levels, p)
    dates_shifted = []

    for date in dates:
        dates_shifted.append(date - d0)

    mpl.style.use('seaborn')

    plt.plot(dates_shifted, levels, '.', label = "actual data")

    x1 = np.linspace(dates_shifted[0], dates_shifted[-1], 30)
    plt.plot(x1, poly(x1), label = "polynomial fit of order {}".format(p))

    plt.plot(x1, high, 'r--', label = "typical range")
    plt.plot(x1, low, 'r--')

    plt.ylabel("water level for {}".format(station.name))
    plt.xlabel("days passed")
    plt.legend()

    plt.show()