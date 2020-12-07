'''
disruption end-point
https://api.tfl.gov.uk/Line/Mode/{modes}/Disruption
'''

class Bus:
    def __init__(self):
        self.end_point = 'https://api.tfl.gov.uk/Line/Route'

    def fetch_all(self):
        pass
