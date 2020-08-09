import tweepy
from HelperClasses.Authentication import Authentication
from HelperClasses.TweetResults import TweetResults
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from datetime import date, timedelta

"""Plots the locations of the given result set on a map of the world"""
def drawMap(results, date):
    plt.title(date)
    plt.figure(figsize=(12, 8))

    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_global()
    ax.stock_img()
    ax.coastlines()

    for tweet in results:
        if tweet.user.baseData.location != "":
            if tweet.user.coordinates is not None:
                lat = tweet.user.coordinates[0]
                long = tweet.user.coordinates[1]
                plt.plot(long, lat, markersize=4, marker='o', color='red')

    plt.savefig("{0}.png".format(date))


api = Authentication().api

mainTag = "covid19"
resultCount = 20

for i in range(1, 8):
    startDate = date.today() - timedelta(days=i)

    tweets = tweepy.Cursor(api.search, q=mainTag, until=startDate, tweet_mode='extended', lang="en").items(resultCount)

    resultData = TweetResults(tweets)
    drawMap(resultData.tweets, startDate)







