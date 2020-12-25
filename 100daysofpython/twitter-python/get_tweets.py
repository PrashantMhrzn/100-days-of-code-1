from create_bot import create_bot


def get_tweets(bot, username):
    for tweet in bot().user_timeline(username):
        print(tweet.text)


get_tweets(create_bot, 'RONBupdates')
