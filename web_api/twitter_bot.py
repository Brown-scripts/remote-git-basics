import tweepy
import os
from dotenv import load_dotenv

api_key=os.getenv('api_key')
secret_key=os.getenv('secret_key')
access_token= os.getenv('access_token')
access_token_secret=os.getenv('access_token_secret')


import tweepy
client = tweepy.Client(consumer_key=api_key,
                    consumer_secret=secret_key,
                    access_token=access_token,
                    access_token_secret=access_token_secret)
# Replace the text with whatever you want to Tweet about
response = client.create_tweet(text='New Tweet')