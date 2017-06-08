import tweepy
from textblob import TextBlob

consumer_key = 'SoEqj9JR0Jxpr9nI5dU438X7B'
consumer_secret = 'ldQ7jDcjI13KczpabbTuttWelne6iGYd3cjcelUsX6KSbZ2Wdi'

access_token = '872425231389868032-vpoVFycAiIy6DctH9dPkKk6f0LXUzN1'
acess_token_secret = 'zh25R6v9qmUu53UtHoUtDxPj9JWo4Ig9pHmmBjJM6C1KA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acess_token_secret)

api = tweepy.API(auth)


public_tweets = api.search('@ScandalABC')

sentiment = 0.00

for tweet in public_tweets:
	analysis = TextBlob(tweet.text)
	sentiment = sentiment + analysis.sentiment.polarity

if sentiment > 0.00:
	print (" ")
	print (" ------ Would recommend @ScandalABC :) ------ ")
	print (" ")
else:
	print "Would not recommend @ScandalABC :("
	

