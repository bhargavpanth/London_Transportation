'''
where mode are ['bus', 'cable-car', 'coach', 'cycle', 'dlr', 'tube', 'walking', 'tube', 'tram', 'tflrail', 'taxi', 'river-tour', 'river-bus', 'replacement-bus', 'overground', 'national-rail', 'interchange-secure', 'interchange-keep-sitting']
fetch modes - https://api.tfl.gov.uk/Line/Meta/Modes
'''
from typing import List
import requests
import json

def get_transportation_modes() -> List[str] or None:
    url = 'https://api.tfl.gov.uk/Line/Meta/Modes'
    res = requests.get(url)
    if res.status_code == 200:
        data = json.loads(res.content.decode('utf-8'))
        return fetch_modes_from_response(data)
    else:
        return None

def fetch_modes_from_response(data) -> List[str] or None:
    modes = []
    for mode in data:
        modes.append(mode['modeName'])
    return modes
