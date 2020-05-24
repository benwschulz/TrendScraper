import tweepy



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search, q="covid19", lang="en", count=10).items(10)

for tweet in tweets:
    print(tweet.text)




















