import tweepy
from HelperClasses.Authentication import Authentication
from HelperClasses.TweetResults import TweetResults
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

api = Authentication().api

mainTag = "covid19"
resultCount = 20
tweets = tweepy.Cursor(api.search, q=mainTag, tweet_mode='extended', lang="en").items(resultCount)

fig = plt.figure(figsize=(12, 8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_global()
ax.stock_img()
ax.coastlines()
plt.title('#' + mainTag)

resultData = TweetResults(tweets)

for tweet in resultData.tweets:
    if tweet.user.baseData.location != "":
        if tweet.user.coordinates is not None:
            lat = tweet.user.coordinates[0]
            long = tweet.user.coordinates[1]
            plt.plot(long, lat, markersize=4, marker='o', color='red')
            print(tweet.user.baseData.location, ":", tweet.text)
            print("")

plt.show()









