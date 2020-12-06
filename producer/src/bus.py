'''
disruption end-point
https://api.tfl.gov.uk/Line/Mode/{modes}/Disruption
where mode are ['bus', 'cable-car', 'coach', 'cycle', 'dlr', 'tube', 'walking', 'tube', 'tram', 'tflrail', 'taxi', 'river-tour', 'river-bus', 'replacement-bus', 'overground', 'national-rail', 'interchange-secure', 'interchange-keep-sitting']
fetch modes - https://api.tfl.gov.uk/Line/Meta/Modes
'''

class Bus:
    def __init__(self):
        self.end_point = 'https://api.tfl.gov.uk/Line/Route'

    def fetch_all(self):
        pass
