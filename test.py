
import tweepy
import config
import time
import sys
import calendar
import datetime

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)

#data = api.get_user('Myst3rie')
user = 'Myst3rie'

def limitReachSleep():
  limit = api.rate_limit_status()['resources']['followers']['/followers/list']
  reset_time = int(limit['reset'])
  cur_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
  try_again_time = reset_time - cur_time + 5
  print 'Limit :( ... ', try_again_time
  time.sleep(try_again_time)


followerIds = list()
current_cursor = -1

while True:
  try:
    curIt = tweepy.Cursor(api.followers, screen_name=user, \
      cursor=current_cursor).pages()
    current_cursor = curIt.next_cursor

    for c in curIt:
      for f in c:
        followerIds.append(f.screen_name)
      print 'lol', len(followerIds)
  except tweepy.error.TweepError, e:
    if e.reason.find('Rate limit exceeded') != -1:
      limitReachSleep()

print 'DBG'
print len(followerIds)
print followerIds
print len(followerIds)
