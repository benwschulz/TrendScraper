from HelperClasses.TweetData import TweetData


class TweetResults:
    """Displays, modifies, parses, and analyzes a given result set"""

    def __init__(self, searchResults):
        self.tweets = []
        self.hashtags = []
        self.gettweetdata(searchResults)
        self.gethashtags(searchResults)  # All unique hashtags in these tweets

    """Converts the list of incoming tweets to a list of type TweetData"""
    def gettweetdata(self, searchResults):
        for tweet in searchResults:
            self.tweets.append(TweetData(tweet))

    """Gets all unique hashtags in a list of tweets and converts them to lowercase"""
    def gethashtags(self, searchResults):
        for tweet in self.tweets:
            entities = tweet.baseData.entities.get('hashtags')
            for entity in entities:
                text = entity.get('text').lower()
                if text not in self.hashtags:
                    self.hashtags.append(text)
