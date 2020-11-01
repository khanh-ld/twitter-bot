import tweepy
import time
import os
from os import environ

CONSUMER_KEY = '4MYrtl1abe4XpWAXL4CBShpT1'
CONSUMER_SECRET = 'mlBeex0aYzQJphu4p3xCm4YrT9aAxYiRB0z4wAdthxJ0b9nbqY'
ACCESS_KEY = '998169701502009345-mUN1MbKwhee0ZtWoVUegAQ8iPOS6Lah'
ACCESS_SECRET = 'hCEWkH7g6ki2pRnWl4HwZRZnzmF8qXEx2J67wQ7ukc14g'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id
    
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return
    
def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush = True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld', flush = True)
            print('responding back...', flush = True)
            api.update_status('@' + mention.user.screen_name + '#HelloWord back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)
