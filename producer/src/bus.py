from utils import get_transportation_modes

class Bus:
    def __init__(self):
        self.end_point = 'https://api.tfl.gov.uk/Line/Route'

    def fetch_transportation_mode(self):
        return get_transportation_modes()['bus']

    def fetch_all(self):
        pass
