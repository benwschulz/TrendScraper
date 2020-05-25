from HelperClasses import TweetData

class TweetResults:
    """Displays, modifies, parses, and analyzes a given result set"""

    def __init__(self, tweets):
        self.tweets = []
        self.getTweetData(tweets)
        self.textBodies = (o.text for o in tweets)  # The text of each tweet
        self.users = (u.user for u in tweets)  # The user data for each tweet
        self.hashtags = self.gethashtags(tweets)  # All unique hashtags in these tweets
        self.locations = (c.coordinates for c in tweets)  # All lat/long coordinates in these tweets

    @staticmethod
    # Get all unique hashtags that occur in a specified result set
    def gethashtags(tweets):
        results = []
        entities = (h.entities.get('hashtags') for h in tweets)
        for entity in entities:
            for item in entity:
                results.append(item.get('text').lower())
        return set(results)

    def getTweetData(self, tweets):
        for tweet in tweets:
            self.tweets.append(TweetData(tweet))
