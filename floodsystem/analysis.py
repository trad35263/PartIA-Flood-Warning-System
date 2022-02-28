from .stationdata import build_station_list
from .datafetcher import fetch_measure_levels
import numpy as np
import matplotlib.pyplot as plt

# for Task 2F

def polyfit(dates, levels, p):

    dates_shifted = []
    d0 = dates[-1]

    for date in dates:
        dates_shifted.append(date - d0)

    p_coeff = np.polyfit(dates_shifted, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, d0