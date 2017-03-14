## need this API https://github.com/bear/python-twitter
## this is the API https://pypi.python.org/pypi/twitter


import twitter

import json

 
   
   # XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
   # for these credentials, which you'll need to provide in place of these
   # empty string values that are defined as placeholders.
   # See https://dev.twitter.com/docs/auth/oauth for more information 
   # on Twitter's OAuth implementation.
   
   
   #Put these values in an external python file and import them using the import statement#
   #CONSUMER_KEY = ''
   #CONSUMER_SECRET=''
   #TOKEN='-'
   #TOKEN_SECRET=''
   
import ConfigParser
config=ConfigParser.RawConfigParser()
config.read('tokenstwitter.properties')

CONSUMER_KEY=config.get('twitter','CONSUMER_KEY') 
CONSUMER_SECRET=config.get('twitter','CONSUMER_SECRET') 
TOKEN=config.get('twitter','TOKEN') 
TOKEN_SECRET=config.get('twitter','TOKEN_SECRET') 
   
# auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)

# twitter_api = twitter.Twitter(auth=auth)
#print CONSUMER_KEY

auth=twitter.oauth.OAuth(TOKEN,TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
t = twitter.Twitter(auth=auth)
recent_tweets = t.statuses.user_timeline(screen_name='nohemivog',count=1)
tweets_in_json= json.dumps(recent_tweets, indent=4, sort_keys=True)
tweets_filename='tweets.json'
f=open(tweets_filename,'w')
f.write(tweets_in_json)
f.close()


print "Length of statuses", len(recent_tweets)

## search all tweets with an @word 
##t2 = t.search.tweets(q="party",count=2)
##print (json.dumps(t2, indent=4, sort_keys=True))

