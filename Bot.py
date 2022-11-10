import tweepy
import config as cfg

auth = tweepy.OAuthHandler(cfg.apiKey, cfg.apiSecret)
auth.set_access_token(cfg.accAccessToken, cfg. accAccessTSecret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Twitter API limit for likes per day is a 1000, be careful
limit = 2500

# Just funny to look at a counter, prints to console
i = 1
s = ' likes'

# Use Exclude_Replies=False to like all tweets and replies, be remember only tweets count towards notifications, replies don't
for tweet in tweepy.Cursor(api.user_timeline, screen_name = cfg.userTarget, exclude_replies=True, include_rts=False).items(limit):
    if (tweet.favorited):
        continue

    print (repr(i) + s)
    i = i + 1
    api.create_favorite(id = tweet.id)
    
    # Safeguard
    if (i > 900):
        break
