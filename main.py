import praw
from data import *

def init_connect():
    reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=SECRET_KEY, password=PASSWORD,
                     user_agent=USER_AGENT, username=USERNAME)
    return reddit


def subreddit_scraper(reddit):
    subreddits = reddit.user.subreddits(limit=None)
    
    for subreddit in subreddits:
        print(subreddit)
    

def multireddit_scraper(reddit):
    multireddits = reddit.user.multireddits()

    for multireddit in multireddits:
        print(multireddit)


def main():
    reddit = init_connect()
    print("username: " + str(reddit.user.me()))
    subreddit_scraper(reddit)
    multireddit_scraper(reddit)

main()
