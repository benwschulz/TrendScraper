import datetime

import tweepy
from HelperClasses.Authentication import Authentication
from HelperClasses.TweetResults import TweetResults
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from datetime import datetime, timedelta

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

    plt.savefig("Output/Maps/{0}.png".format(date))

def printText(results, date):
    output = open("Output/Content/{0}.txt".format(date), 'w')

    for tweet in resultData.tweets:
        output.write("{0} ({1})\n".format(str(tweet.baseData.created_at),
                                          tweet.baseData.user.location))
        output.write(tweet.baseData.full_text + '\n')
        output.write("--------------------------")

    output.close()

api = Authentication().api

mainTag = "covid19"
resultCount = 20

# Gets the results for each day in the last ten days (as far back as the public Twitter API allows)
for i in reversed(range(10)):
    # Go back one more day on each iteration
    untilDate = datetime.today() - timedelta(days=i)
    sinceDate = datetime.today() - timedelta(days=i + 1)

    # Format datetime objects as strings
    Since = sinceDate.strftime('%Y-%m-%d %H:%M')
    Until = untilDate.strftime('%Y-%m-%d %H:%M')

    # Gets today
    if i == 0:
        Until = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M')
        Since = (datetime.today()).strftime('%Y-%m-%d %H:%M')

    tweets = tweepy.Cursor(api.search, q=mainTag, since=Since, until=Until,
                           tweet_mode='extended', lang="en").items(resultCount)
    resultData = TweetResults(tweets)

    fileName = sinceDate.strftime('%Y-%m-%d')
    printText(resultData.tweets, fileName)
    drawMap(resultData.tweets, fileName)







