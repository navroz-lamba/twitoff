from tweepy import OAuthHandler, API
import os
from dotenv import load_dotenv 

load_dotenv()

# TWITTER_USERS = ['calebhicks', 'elonmusk', 'rrherr', 'SteveMartinToGo',
#                  'alyankovic', 'nasa', 'sadserver', 'jkhowland', 'austen',
#                  'common_squirrel', 'KenJennings', 'conanobrien',
#                  'big_ben_clock', 'IAM_SHAKESPEARE']

TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')


auth = OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = API(auth)
print("API CLIENT", api)

user = api.get_user('elonmusk')
print("TWITTER USER:", type(user))
print(user.id)
print(user.screen_name)
print(user.name)

tweets = api.user_timeline('elonmusk', tweet_mode='extended')
print("TWEETS", type(tweets))
print(type(tweets[0]))

tweet = tweets[0]
print(tweet.id)
print(tweet.full_text)

breakpoint()