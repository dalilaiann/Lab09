from dataclasses import dataclass


@dataclass

class Flight:
    OriginAirportID:int
    DestinationAirportID:int
    Distance:float

    def __hash__(self):
        return hash((self.OriginAirportID, self.DestinationAirportID))

    def __eq__(self, other):
        return self.OriginAirportID==self.DestinationAirportID and self.DestinationAirportID==self.OriginAirportID
