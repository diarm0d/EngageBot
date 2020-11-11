import tweepy
import time

consumer_key = 'CONSUMER KEY'
consumer_secret = 'CONSUMER SECRET'
access_token = 'ACCESS TOKEN'
access_token_secret = 'ACCESS TOKEN SECRET'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user = api.me()

search = 'HASHTAG'
No_Tweets = 500

for tweet in tweepy.Cursor(api.search, search, lang="en").items(No_Tweets):
	try:
		print('Tweet Liked')
		tweet.favorite()
		time.sleep(30)
	except tweepy.TweepError as e:
		print(e.reason)
	except StopInteration:
		break

