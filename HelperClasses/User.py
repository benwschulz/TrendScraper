class User:
    """Extends the User class with additional functionality and properties"""
    def __init__(self, tweet):
        self.baseData = tweet.user
        self.coordinates = self.getLocationCoordinates()
        self.isBot = self.getBotStatus()

    """Does its best to get the coordinates of this user's location"""
    def getLocationCoordinates(self):
        if (self.baseData.location != ""):
            return ""

        return ""

    """Determines whether this user is a bot or not (many users are, and we don't want to count them)"""
    def getBotStatus(self):
        return False