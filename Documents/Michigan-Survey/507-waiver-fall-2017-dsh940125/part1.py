# these should be the only imports you need
import tweepy
import nltk
import json
import sys
import operator
from tweepy.auth import OAuthHandler

# write your code here
# usage should be python3 part1.py <username> <num_tweets>

CONSUMER_KEY = 'XXX' 		
CONSUMER_SECRET = 'XXX' 	
ACCESS_TOKEN = 'XXX' 	
ACCESS_TOKEN_SECRET = 'XXX'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def analyze_tweets(username, num_tweets):
    fetched_tweets = []
    tweet_text = []
    original = []
    nouns = {}
    adjs = {}
    verbs = {}
    stop_word = ['http','https','RT']
    favor = 0
    retwee = 0
    tweets = api.user_timeline(id=username,count=num_tweets,tweet_mode="extended",include_rts=True) # Fetch the required tweets
    if tweets: 
        for tweet in tweets:
            json_tweet = tweet._json 
            fetched_tweets.append(json_tweet)
            tweet_text.append(tweet.full_text)
            if not tweet.full_text.startswith("RT"):
                original.append(json_tweet)
        if len(fetched_tweets) < eval(num_tweets):
            print("No enough tweets") # Do only if there are enough tweets
        else:
            # Analyze the tweets
            for text in tweet_text:
                tokens = nltk.word_tokenize(text)
                tagged_tokens = nltk.pos_tag(tokens)
                for item,tag in tagged_tokens:
                    if item[0].isalpha() and item not in stop_word:
                        if tag in ['NN','NNS','NNP','NNPS']:
                            nouns[item] = nouns.get(item, 0) +1
                        if tag in ['JJ','JJR','JJS']:
                            adjs[item] = adjs.get(item, 0) +1
                        if tag in ['VB','VBD','VBG','VBN','VBP','VBZ']:
                            verbs[item] = adjs.get(item, 0) +1
            sorted_nouns = sorted(nouns.items(), key=operator.itemgetter(1), reverse = True)
            sorted_adjs = sorted(adjs.items(), key=operator.itemgetter(1), reverse = True)
            sorted_verbs = sorted(verbs.items(), key=operator.itemgetter(1), reverse = True)
            # Favorited and retweeted counts
            for t in original:
                favor += t["favorite_count"]
                retwee += t["retweet_count"]
            print('USER: {}'.format(username))
            print('TWEETS ANALYZED: {}'.format(num_tweets))
            print('VERBS: {} ({}) {} ({}) {} ({}) {} ({}) {} ({})'.format(sorted_verbs[0][0],  sorted_verbs[0][1], sorted_verbs[1][0], sorted_verbs[1][1], sorted_verbs[2][0],  sorted_verbs[2][1], sorted_verbs[3][0],  sorted_verbs[3][1], sorted_verbs[4][0],  sorted_verbs[4][1]))
            print('NOUNS: {} ({}) {} ({}) {} ({}) {} ({}) {} ({})'.format(sorted_nouns[0][0],  sorted_nouns[0][1], sorted_nouns[1][0], sorted_nouns[1][1], sorted_nouns[2][0],  sorted_nouns[2][1], sorted_nouns[3][0],  sorted_nouns[3][1], sorted_nouns[4][0],  sorted_nouns[4][1]))
            print('ADJECTIVES: {} ({}) {} ({}) {} ({}) {} ({}) {} ({})'.format(sorted_adjs[0][0],  sorted_adjs[0][1], sorted_adjs[1][0], sorted_adjs[1][1], sorted_adjs[2][0],  sorted_adjs[2][1], sorted_adjs[3][0],  sorted_adjs[3][1], sorted_adjs[4][0],  sorted_adjs[4][1]))
            print('ORIGINAL TWEETS: {}'.format(len(original)))
            print('TIMES FAVORITED (ORIGINAL TWEETS ONLY): {}'.format(favor))
            print('TIMES RETWEETED (ORIGINAL TWEETS ONLY): {}'.format(retwee))
    else:
        print("No tweets")



if __name__ == '__main__':
    analyze_tweets(input(), input())
