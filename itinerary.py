class Itinerary:
    def __init__(self):
        self.citylist=[]
        self.distance=0
        self.startdate=''    
    
class ItineraryCity:
    def __init__(self):
        self.id=0
        self.name=''
        self.longitude=0
        self.latitude=0
        self.description=''
        self.placelist=[]
        self.date=''

class ItineraryPlace:
    def __init__(self):
        self.placeid=0
        self.name=''
        self.longitude=0
        self.latitude=0
        self.description=''
        self.datetime=''
        self.tags=[]
