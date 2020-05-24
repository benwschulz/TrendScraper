import tweepy


# noinspection SpellCheckingInspection
class Authentication:
    """Initializes a connection to Twitter and its API class"""
    def __init__(self):
        consumer_key = "KhYTSB3pIQQDcUz0IVJIic1CI"
        consumer_secret = "D1raAZPBZnTTGGpRky6evgCIdIDJv5Hkxtgur7gZmHw0ffcjOT"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.access_token_secret = "I3plHF0ObiWdnYcL4udQDbl2oWvdlxj9lTJRCl5hS17gY"
        self.access_token_key = "1264304925263224832-3rTlvR46Vnym1K1reKAAWmUZbPDOXG"
        self.api = tweepy.API(auth)
