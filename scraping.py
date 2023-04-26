
import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:benshapiro) until:2017-01-01 since:2016-01-01"
tweets = []
limit = 500


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date,tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# to save to csv
df.to_csv('tweets.csv')