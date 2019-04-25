#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
philippineFlag = u'\U0001F1F5' + u'\U0001F1ED'

filenames = []
for element in sys.argv[3:]:
  filenames.append(element)

media_ids = []
for filename in filenames:
  res = api.media_upload(filename)
  media_ids.append(res.media_id)

api.update_status(status=philippineFlag + ' Image from satellite: ' + sys.argv[1] + '. Max elevation: ' + sys.argv[2] + ' degrees. #NOAA #weather #noaasatellite #climate #wxtoimg #raspberrypi #philippines #pagasa', media_ids=media_ids)
