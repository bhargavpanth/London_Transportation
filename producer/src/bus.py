'''
disruption end-point
https://api.tfl.gov.uk/Line/Mode/{modes}/Disruption
'''
from utils import get_transportation_modes

class Bus:
    def __init__(self):
        self.end_point = 'https://api.tfl.gov.uk/Line/Route'

    def fetch_transportation_mode(self):
        if get_transportation_modes().index('Bus'):
            return 'Bus'
        return 'Bus'

    def fetch_all(self):
        pass
