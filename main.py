import praw
from data import *


def main():
    reddit = init_connect()
    print(reddit)
    print(reddit.read_only)
    print(reddit.user.me())
    print(praw.models.User.subreddits)


def init_connect():
    reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=SECRET_KEY, password=PASSWORD,
                     user_agent=USER_AGENT, username=USERNAME)
    return reddit


main()
