import praw
from data import *

def init_connect():
    reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=SECRET_KEY, password=PASSWORD,
                     user_agent=USER_AGENT, username=USERNAME)
    return reddit


def test(reddit):
    subreddits = reddit.user.subreddits(limit=None)
    counter = 0
    
    for subreddit in subreddits:
        counter = counter + 1
        print(counter)
        print(subreddit)
    

def main():
    reddit = init_connect()
    print("username: " + str(reddit.user.me()))
    test(reddit)

main()
