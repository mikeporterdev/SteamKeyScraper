'''
Created on 1 Nov 2014

@author: michael
'''
import praw
import re
#from pushbullet import PushBullet
from settings import api_key
    

#def pushToDevices(title, key):
#    pb = PushBullet(api_key)
#    phone = pb.push_note(title, key)
#    print(phone.status_code)
    
def getKey(post):
    code = re.findall(r'[A-Z0-9]+-[A-Z0-9]+-[A-Z0-9]+', post)  
    return code

def scrapeSubreddit(connection, subreddit):

    submissions = connection.get_subreddit(subreddit).get_new(limit=100)
    
    for submission in submissions:
        post = vars(submission)
        body = post['selftext']
        keys = getKey(body)
        if keys:      
            #pushToDevices(str(submission), keys)     
            print(str(submission))
            print(keys)

def main():
    r = praw.Reddit(user_agent = "Steam Key Scraper")
    subreddits = ['pcgaming', 'gaming', 'steam', 'games']
    for subreddit in subreddits:
        print(subreddit)
        scrapeSubreddit(r, subreddit)


if __name__ == '__main__':
    main()
