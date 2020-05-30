from HelperClasses.Authentication import Authentication
from HelperClasses.TweetResults import TweetResults
import tweepy


api = Authentication().api

mainTag = "covid19"
resultCount = 10

tweets = tweepy.Cursor(api.search, q=mainTag, lang="en").items(resultCount)

resultData = TweetResults(tweets)

#for tag in resultData.hashtags:
 #   print(tag)

for tweet in resultData.tweets:
    if tweet.user.coordinates != "":
        print(tweet.user.coordinates)


















