from geopy.geocoders import Nominatim


class User:
    """Extends the User class with additional functionality and properties"""

    def __init__(self, tweet):
        self.baseData = tweet.user
        self.coordinates = self.getLocationCoordinates
        self.isBot = self.getBotStatus()

    """Does its best to get the coordinates of this user's location"""
    @property
    def getLocationCoordinates(self):
        if self.baseData.location != "":
            geolocator = Nominatim(user_agent="TrendScraper")
            try:
                location = geolocator.geocode(self.baseData.location)
                return [location.latitude, location.longitude]
                #return str((location.latitude, location.longitude))

            except:
                pass

    """Determines whether this user is a bot or not (many users are, and we don't want to count them)"""
    def getBotStatus(self):
        return False
