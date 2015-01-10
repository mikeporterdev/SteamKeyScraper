'''
Created on 1 Nov 2014

@author: michael
'''
import praw
import re
import time

from settings import pushbullet, api_key, subreddits

def pushToDevices(postTitle, key):
    import requests
    data = {
            "type" : "note",
            "title" : postTitle,
            "body" : key
            }
    requests.post('https://api.pushbullet.com/v2/pushes', auth=(api_key, ''), data=data)

def getKey(post):
    code = re.findall(r'(\w{5}-){2}\w{5}', post)  
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
                    for title in key:
                        if pushbullet:
                            pushToDevices(title, key[title])
                        else:
                            print(title, key[title])
        time.sleep(31)

if __name__ == '__main__':
    main()
