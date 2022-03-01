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

# for Task 2G

def predict_future_level(dates, levels):
    assert len(dates) == len(levels)
    assert len(dates) > 0

    x = matplotlib.dates.date2num(dates)
    d0 = sum(x) / len(x)
    coeff = np.polyfit(x - d0, levels, 3)
    poly = np.poly1d(coeff)

    # one day after the most recent day
    future_date = max(x) + 1
    return matplotlib.dates.num2date(future_date), poly(future_date - d0)