import os
from dotenv import load_dotenv
from tweepy import OAuthHandler, API

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
TWITTER_ACCESS_TOKEN = os.getenv("ACCESS_KEY")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("SECRET_ACCESS_KEY")

auth = OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("API AUTH:", auth)
api = API(auth)
print("API CLIENT", api)

if __name__ == "__main__":

    user = api.get_user('s2t2')
    print("TWITTER USER:", type(user))

    tweets = api.user_timeline("s2t2", tweet_mode="extended")


    tweet = tweets[0]

    print(tweet.id)
    print(tweet.full_text)

    breakpoint()
    ## set up views and routes to help us explore the twitter api
