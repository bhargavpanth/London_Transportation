from utils import get_transportation_modes, disruption_for_mode, Mode
# from lib.kafka_producer_consumer import Producer, Consumer

class Bus:
    def __init__(self):
        # route id starts from 100
        self.end_point = 'https://api.tfl.gov.uk/Line/Route'

    def fetch_transportation_mode(self):
        return get_transportation_modes()['bus']

    def fetch_all(self):
        pass

    def get_disruption(self):
        model = disruption_for_mode(Mode.BUS)
