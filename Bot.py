import tweepy
import time
import config as cfg

auth = tweepy.OAuthHandler(cfg.apiKey, cfg.apiSecret)
auth.set_access_token(cfg.accAccessToken, cfg. accAccessTSecret)
api = tweepy.API(auth, wait_on_rate_limit=True)

limit = 10
i = 1
s = ' likes'

# Use Exclude_Replies for a cooler twitter notification
for tweet in tweepy.Cursor(api.user_timeline, screen_name = cfg.userTarget, include_rts=False).items(limit):
    if (tweet.favorited == True):
        continue
    print (repr(i) + s)
    i = i + 1
    api.create_favorite(id = tweet.id)