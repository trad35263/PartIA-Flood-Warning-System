import datetime
from .stationdata import build_station_list
from .datafetcher import fetch_measure_levels
import numpy as np
import matplotlib.pyplot as plt

# for Task 2F

def polyfit(dates, levels, p):

    p_coeff = np.polyfit(dates, levels, p)

    poly = np.poly1d(p_coeff)

    plt.plot(dates, levels, '.')

    x1 = np.linspace(dates[0], dates[-1], 30)
    plt.plot(x1, poly(x1))

    plt.show()