# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from .stationdata import build_station_list

import math

# for task 1B

def haversine(p, coord):
    lon1,lat1 = p
    lon2,lat2 = coord
    
    r = 6371000
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi/2.0)**2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
    return r * c / 1000


def stations_by_distance(stations, p):

    station_names = []
    station_coords = []
    station_towns = []
    distances = []

    for station in stations:
        station_names.append(station.name)
        station_coords.append(station.coord)
        station_towns.append(station.town)

    for i in range(len(station_coords)):
        distances.append(haversine(station_coords[i], p))
    
    output = list(zip(station_names, station_towns, distances))
    return sorted_by_key(output, 2)

# for task 1C 

def stations_within_radius(stations, centre, r):
    stations_within_radius = []
    for station in stations:
        if haversine(station.coord, centre) <= r:
            stations_within_radius.append(station.name)
    return stations_within_radius 
        


# for task 1D

def rivers_with_station(stations):

    rivers_with_station = set()

    for station in stations:
        rivers_with_station.add(station.river)

    return sorted(rivers_with_station)

def stations_by_river(stations):
    
    station_river_dict = dict()

    for station in stations:
        if station.river in station_river_dict:
            x = station_river_dict[station.river].append(station.name) # removing this entirely useless line of code breaks the whole thing ??? ideally would be replaced with a pass statement
        else:
            station_river_dict.update({station.river: [station.name]})

    return station_river_dict