# import packages
import pip
import tweepy
import time



# Authenticate to Twitter
consumer_key = 'kh5NJemqbiBM3slZBaFqvIg3W'
consumer_secret = '44GZfZmdyUq7QiSMBexNMMMTsDn503ioKYFdTy4USqenD4ITYV'
access_key = '1507463150559535109-sjFJpCvIQAbeQ8FbLi3RkRmorBmXc2'
access_secret = 'KYdaK1agVoyGDc1pzeY9f8Vdacf1ljA7HGajuC252ijbi'


#Create API oject
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)

user = api.get_user
search = 'womenintech'
num_of_tweets = 1000

for tweet in tweepy.Cursor(api.search_tweets, search).items(num_of_tweets):
    try:
        tweet.retweet()
        print('Retweet')
        time.sleep(0)
    except tweepy.errors.TweepError as e:
        print(e.reason)
    except StopIteration:
        break