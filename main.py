'''
Created on 1 Nov 2014

@author: michael
'''
import praw
import re
import time
from pprint import pprint

from settings import api_key, subreddits


#from pushbullet import PushBullet
#def pushToDevices(title, key):
#    pb = PushBullet(api_key)
#    phone = pb.push_note(title, key)
#    print(phone.status_code)

def getKey(post):
    code = re.findall(r'[A-Z0-9]+-[A-Z0-9]+-[A-Z0-9]+', post)  
    return code

def scrapeSubreddit(connection, subreddit):

    submissions = connection.get_subreddit(subreddit).get_new(limit=25)
    keysList = []
    for submission in submissions:
        post = vars(submission)
        title = post['title']
        body = post['selftext']
        keys = getKey(body)
        if keys:      
            #pushToDevices(str(submission), keys)
            keysList.append({title : keys})
    return keysList
    


def main():
    r = praw.Reddit(user_agent = "Steam Key Scraper")
    keys = []
    while True:
        for subreddit in subreddits:
            key = scrapeSubreddit(r, subreddit)
            if key:
                if not key in keys:
                    keys.append(key)
                    print(key)
        time.sleep(31)

if __name__ == '__main__':
    main()
