from HelperClasses.User import User


class TweetData:
    """Extends the Tweet class with additional functionality and properties"""

    def __init__(self, tweet):
        self.baseData = tweet
        self.text = ""
        self.getAllText()
        self.comments = []
        self.getcomments()
        self.user = User(tweet)

    def getAllText(self):
        try:
            self.text = self.baseData.retweeted_status.full_text
        except:
            self.text = self.baseData.full_text

    """Gets all comments for this tweet"""
    def getcomments(self):
        entities = self.baseData.entities.get('hashtags')
        self.comments.append("test")
