#from .stationdata import build_station_list
#from .datafetcher import fetch_measure_levels
import numpy as np
import matplotlib
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

# for Task 2G

def predict_future_level(dates, levels):
    assert len(dates) == len(levels)
    assert len(dates) > 0

    poly, d0 = polyfit(dates, levels, 2)

    future_date = dates[0] + 1
    return poly(future_date - d0)