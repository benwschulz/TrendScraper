from HelperClasses.Authentication import Authentication
from HelperClasses.TweetResults import TweetResults
import tweepy

#import cartopy.crs as ccrs                   # import projections
#import cartopy.feature as cf                 # import features
#ax = plt.axes(projection = ccrs.Mercator())  # create a set of axes with Mercator projection
#ax.add_feature(cf.COASTLINE)                 # plot some data on them
#ax.set_title("Title")                        # label it
#plt.show()

api = Authentication().api

mainTag = "georgefloyd"
resultCount = 100

tweets = tweepy.Cursor(api.search, q=mainTag, tweet_mode='extended', lang="en").items(resultCount)

resultData = TweetResults(tweets)
#also add functionality for Twitter API Place object

for tweet in resultData.tweets:
    if tweet.user.baseData.location != "":
        print(tweet.user.baseData.location)


















