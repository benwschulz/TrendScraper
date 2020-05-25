class TweetData:
    """Extends the Tweet class with additional functionality and properties"""
    def __init__(self, tweet):
        self.tweet = tweet
        self.comments = []
        self.getcomments()

    def getcomments(self):
        self.comments.append("test")