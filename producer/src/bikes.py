from utils import disruption_for_mode, Mode

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

    def __get_disruption_mode(self):
        mode = disruption_for_mode(Mode.CYCLE)