# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 19:41:17 2020

@author: VARUN SAKUNIA
"""

import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

def percentage(part,whole):
    return 100 * float(part)/ float(whole)

#authenticating
consumerKey = '9oyfw8phVoKtKl6QRWRhPAIxP'   #give your values here
consumerSecret = 'oOjSoKvWYRtUIoGZa7tt3ySoVJj5UQNxJ2Txc1FCWJS2LHsa5y'
accessToken = '920163998523203586-YlL0u7LHhOcw0qBrlDuFtVSXKFki6uB'
accessTokenSecret = 'VOz1TINUYQFRSGJnMdZxMBY0Y265VaAYfAbiUu0P10MJ4'

auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret =consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)

#input term

searchTerm = input("Enter keyword/tag to search about:")
NoOfTerms = int(input("Enter how many tweets you want to search"))

#searching for the tweets

tweets = tweepy.Cursor(api.search,q=searchTerm).items(NoOfTerms)

#creating some variables to store info

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    
    if (analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity <= 0.00):
        negative += 1
    elif (analysis.sentiment.polarity >= 0.00):
        positive += 1
        
positive = percentage(positive,NoOfTerms)
negative = percentage(negative,NoOfTerms)
neutral = percentage(neutral,NoOfTerms)
polarity = percentage(polarity,NoOfTerms)

positive = format(positive,'.2f')
negative = format(negative,'.2f')
negative = format(neutral,'.2f')

print("How many people are reacting on" +searchTerm+ "by analyzing" +str(NoOfTerms) + "Tweets")

if (polarity==0):
    print("neutral")
elif (polarity < 0.00):
    print("negarive")
elif (polarity > 0.00):
    print("positive")
    
 #assigning the labels for plotting the graph 
labels = ['Positive['+str(positive)+ '%]','Neutral['+str(neutral) + '%]','Negative[' + str(negative)+'%]']
sizes = [positive,negative,neutral]
colors = ['yellowgreen','blue','red']
patches,text = plt.pie(sizes,colors = colors,startangle=90)
plt.legend(patches,labels,loc = "best")
plt.title("Tweet analysis" +searchTerm+ "with the"+ str(NoOfTerms))
plt.axis('equal')
plt.show()
