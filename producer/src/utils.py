'''
where mode are ['bus', 'cable-car', 'coach', 'cycle', 'dlr', 'tube', 'walking', 'tube', 'tram', 'tflrail', 'taxi', 'river-tour', 'river-bus', 'replacement-bus', 'overground', 'national-rail', 'interchange-secure', 'interchange-keep-sitting']
fetch modes - https://api.tfl.gov.uk/Line/Meta/Modes
'''
from enum import Enum
from typing import List
import requests
import json

class Mode(Enum):
    BUS = 'bus'
    CABLE_CAR = 'cable-car'
    COACH = 'coach'
    CYCLE = 'cycle'
    CYCLE_HIRE = 'cycle-hire'
    DLR = 'dlr'
    INTERCHANGE_KEEP_SITTING = 'interchange-keep-sitting'
    INTERCHANGE_SECURE = 'interchange-secure'
    NATIONAL_RAIL = 'national-rail'
    OVERGROUND = 'overground'
    REPLACEMENT_BUS = 'replacement-bus'
    RIVER_BUS = 'river-bus'
    RIVER_TOUR = 'river-tour'
    TAXI = 'taxi'
    TFL_RAIL = 'tflrail'
    TRAM = 'tram'
    TUBE = 'tube'
    WALKING = 'walking'


def get_transportation_modes() -> List[str] or None:
    url = 'https://api.tfl.gov.uk/Line/Meta/Modes'
    res = requests.get(url)
    if res.status_code == 200:
        data = json.loads(res.content.decode('utf-8'))
        return fetch_modes_from_response(data)
    else:
        return None

def fetch_modes_from_response(data) -> List[str] or None:
    modes = {}
    for mode in data:
        modes[mode['modeName']] = mode['modeName']
    return modes

def disruption_for_mode(mode: Mode):
    if not mode:
        return None
    url = f'https://api.tfl.gov.uk/Line/Mode/{mode}/Disruption'
    res = requests.get(url)
    if res.status_code == 200:
        data = json.loads(res.content.decode('utf-8'))
        return data
    else:
        return None
