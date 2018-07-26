"""
    instabot example

    Workflow:
        Like and follow users who liked the last media of input users.
"""

import argparse
import os
import sys
import random

from tqdm import tqdm

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

competitors_list = bot.read_list_from_file("follow_followers.txt")

for username in competitors_list:
    medias = bot.get_user_medias(username, filtration=False)
    if len(medias):

        likers = bot.get_media_likers(medias[0])

        #at most, pick 50 users from each person
        if len(likers) > 50:
            likers = likers[0:50]

        for liker in tqdm(likers):
            bot.like_user(liker, amount=2)

            #only follow 20% of users, like all the rest
            if random.randint(1,11) <= 2:
                bot.follow(liker)
