import praw

from data import *

# initializes a Reddit instance which connects the script with reddit
def init_connect(client_id, secret_key, password, user_agent, username):
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=secret_key, password=password,
                         user_agent=user_agent, username=username)
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
        subreddits = subreddits + multireddit_data

    return subreddits


# extracts the name of the multireddit
def multireddit_name(multireddit):
    words = str(multireddit).split("/")
    return words[4]


# extracts the name of the subreddit in a multireddit
def multireddit_data_extractor(data):
    display_name = []

    for subreddit in data:
        result = str(subreddit).split("\'")
        result = result[0]
        display_name.append(result)

    return display_name


# subscribes the target user to the extracted subreddits
def subreddit_subscriber(subreddits):
    target_reddit = init_connect(TARGET_CLIENT_ID, TARGET_SECRET_KEY,
                          TARGET_PASSWORD, TARGET_USER_AGENT, TARGET_USERNAME)
    print("Target username: " + str(target_reddit.user.me()))
    for subreddit in subreddits:
        print(subreddit)
        display_name = target_reddit.subreddit(str(subreddit))
        print("Is subscribed: " + str(display_name.user_is_subscriber))
        if not display_name.user_is_subscriber:
            display_name.subscribe()


# what main handler of the program
def main():
    reddit = init_connect(CLIENT_ID, SECRET_KEY,
                          PASSWORD, USER_AGENT, USERNAME)
    print("Username: " + str(reddit.user.me()))

    subreddit = subreddit_scraper(reddit)
    multireddit = multireddit_scraper(reddit)
    multireddit_subreddits = multireddit_extractor(reddit, multireddit)
    subreddit_subscriber(subreddit + multireddit_subreddits)

    print("Done")


main()
