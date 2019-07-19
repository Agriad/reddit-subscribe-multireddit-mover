import praw
import re

from data import *

# initializes a Reddit instance which connects the script with reddit
def init_connect():
    reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=SECRET_KEY, password=PASSWORD,
                     user_agent=USER_AGENT, username=USERNAME)
    return reddit


# extracts subreddits that the user is subscribed to
def subreddit_scraper(reddit):
    subreddits = reddit.user.subreddits(limit=None)
    list_subreddit = []
    
    for subreddit in subreddits:
        list_subreddit.append(subreddit)

    return list_subreddit
    

# extracts the multireddits that the user created
def multireddit_scraper(reddit):
    multireddits = reddit.user.multireddits()
    list_multireddit = []

    for multireddit in multireddits:
        list_multireddit.append(multireddit)

    return list_multireddit


# finds the list of subreddits in the multireddit and returns it neatly
def multireddit_extractor(reddit, multireddits):
    subreddits = []

    for multireddit in multireddits:
        name = multireddit_name(multireddit)
        multireddit_data = reddit.multireddit(USERNAME, name).subreddits
        # multireddit_extract = multireddit_data_extractor(multireddit_data)
        # subreddits = subreddits + multireddit_extract
        subreddits = subreddits + multireddit_data

    return subreddits


# extracts the name of the multireddit
def multireddit_name(multireddit):
    words = str(multireddit).split("/")
    return words[4]


# exrtacts the name of the subreddit in a multireddit
def multireddit_data_extractor(data):
    display_name = []

    for subreddit in data:
        result = str(subreddit).split("\'")
        result = result[0]
        display_name.append(result)

    return display_name

# what main handler of the program
def main():
    reddit = init_connect()
    print("username: " + str(reddit.user.me()))

    subreddit = subreddit_scraper(reddit)
    multireddit = multireddit_scraper(reddit)
    multireddit_subreddits = multireddit_extractor(reddit, multireddit)

    print(subreddit + multireddit_subreddits)


main()
