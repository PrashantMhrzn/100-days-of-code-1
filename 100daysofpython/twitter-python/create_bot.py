import os
import tweepy
from dotenv import load_dotenv
from pathlib import Path


def create_bot():
    # Loads environment variables
    env_path = Path('./config')/'.env'
    load_dotenv(dotenv_path=env_path)
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET_KEY = os.getenv('CONSUMER_KEY_SECRET')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

    # Authenticate user
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # INIT
    api = tweepy.API(auth)
    return api
