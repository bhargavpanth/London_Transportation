'''
where mode are ['bus', 'cable-car', 'coach', 'cycle', 'dlr', 'tube', 'walking', 'tube', 'tram', 'tflrail', 'taxi', 'river-tour', 'river-bus', 'replacement-bus', 'overground', 'national-rail', 'interchange-secure', 'interchange-keep-sitting']
fetch modes - https://api.tfl.gov.uk/Line/Meta/Modes
'''
import urllib

def get_transportation_modes():
    url = 'https://api.tfl.gov.uk/Line/Meta/Modes'
    req = urllib.request.Request(url)
    pass
