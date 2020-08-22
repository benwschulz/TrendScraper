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

"""Prints out the text of each tweet in the set in a readable format"""
def printText(results, date):
    output = open("Output/Content/{0}.txt".format(date), 'w')

    for tweet in resultData.tweets:
        location = tweet.baseData.user.location
        printLocation = "No Location" if not location else location

        output.write("----------------------------{0}----------------------------\n".format(printLocation))
        output.write(tweet.baseData.full_text + '\n')

    output.close()

# Connect to Twitter API
api = Authentication().api

mainTag = "covid19"
resultCount = 20

# Gets the results for each day in the last seven days (as far back as the public Twitter API allows)
for i in reversed(range(7)):
    # On the last iteration of this loop, get today
    if i == 0:
        until = (datetime.today() + timedelta(days=1))
        since = (datetime.today())
    else:
        # Go back one more day on each iteration
        until = datetime.today() - timedelta(days=i)
        since = datetime.today() - timedelta(days=i + 1)

    # Format datetime objects as strings
    EndDate = until.strftime('%Y-%m-%d %H:%M')
    StartDate = since.strftime('%Y-%m-%d %H:%M')

    tweets = tweepy.Cursor(api.search, q=mainTag, since=StartDate, until=EndDate,
                           tweet_mode='extended', lang="en").items(resultCount)

    resultData = TweetResults(tweets)

    # Create output
    fileName = StartDate
    printText(resultData.tweets, fileName)
    drawMap(resultData.tweets, fileName)







