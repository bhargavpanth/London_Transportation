from utils import disruption_for_mode, Mode
from lib.kafka_producer_consumer import Producer, Consumer

class Bike:
    def __init__(self):
        self.end_point = 'https://api.tfl.gov.uk/BikePoint'

    def fetch_all(self):
        # GET req on self.end_point
        pass

    def get_data_by_bike_point_id(self, id: str):
        # GET req on f'{self.endpoint}/{id}'
        # where id is f'Bikepoints_{num}' and 1 <= num <= 821
        pass

    def get_disruption(self):
        mode = disruption_for_mode(Mode.CYCLE)