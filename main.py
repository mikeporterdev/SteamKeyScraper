'''
Created on 1 Nov 2014

@author: michael
'''
import praw
import re
    
    
def get_key(post):
    #keyMatch = re.compile("r'[A-Z0-9]+-[A-Z0-9]+-[A-Z0-9]+'")   
    #reg = re.match(keyMatch, "A2DL3-23SOD-23LKS")
    code = re.findall(r'[A-Z0-9]+-[A-Z0-9]+-[A-Z0-9]+', post)  
    return code

def main():
    r = praw.Reddit(user_agent = "Praw Test")
    submissions = r.get_subreddit('Gaming').get_new(limit=100)
    
    for submission in submissions:
        things = vars(submission)
        body = things['selftext']
        keys = get_key(body)
        if keys:
            print(submission)
            print(keys)            

if __name__ == '__main__':
    main()
