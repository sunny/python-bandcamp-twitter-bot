#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import tweepy

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

def tweet(message):
  # Authenticate to Twitter
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  # Create API object
  api = tweepy.API(auth)

  # Create a tweet
  api.update_status(message)