'''
Created on 1 Nov 2014

@author: michael
'''
import praw
import re
import time

from settings import api_key, subreddits

def pushToDevices(postTitle, key):
    import requests
    #data=dict(device_id='OnePlus A0001', title=postTitle, body=key, type='note')
    #requests.post('https://www.pushbullet.com/v2/', auth=(api_key,''), data=data)
    #devices = requests.get('https://api.pushbullet.com/v2/devices', auth=(api_key, '')).json()
    #deviceid = devices['devices'][2]['iden']
    data = {
            "type" : "note",
            "title" : postTitle,
            "body" : key
            }
    push = requests.post('https://api.pushbullet.com/v2/pushes', auth=(api_key, ''), data=data)
    print(push.json())

def getKey(post):
    code = re.findall(r'[A-Z0-9]+-[A-Z0-9]+-[A-Z0-9]+', post)  
    return code

def scrapeSubreddit(connection, subreddit):

    submissions = connection.get_subreddit(subreddit).get_new(limit=25)
    keysList = {}
    for submission in submissions:
        post = vars(submission)
        title = post['title']
        body = post['selftext']
        keys = getKey(body)
        if keys:      
            #pushToDevices(str(submission), keys)
            keysList[title] = keys
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
                    for thing in key:
                        pushToDevices(thing, key[thing])
        time.sleep(31)

if __name__ == '__main__':
    main()
