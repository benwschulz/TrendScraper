from HelperClasses.Authentication import Authentication
from HelperClasses.TweetResults import TweetResults
import tweepy

api = Authentication().api
mainTag = "covid19"

tweets = tweepy.Cursor(api.search, q=mainTag, lang="en", count=10).items(100)

resultData = TweetResults(tweets)

for tag in resultData.hashtags:
    print(tag)




















