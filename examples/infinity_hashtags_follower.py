"""
    instabot example

    Workflow:
        Follow users who post medias with hashtag.
"""

import argparse
import os
import sys
import time
from random import shuffle


sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)

like_hashtags_list = bot.read_list_from_file("like_hashtags.txt")

all_users = []



for hashtag in like_hashtags_list:
    users = bot.get_hashtag_users(hashtag)
    all_users += users

#randomization routine
shuffle(all_users)

bot.follow_users(users)
time.sleep(10)
