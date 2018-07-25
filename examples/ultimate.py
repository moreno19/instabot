"""
    ULTIMATE SCRIPT

    It uses data written in files:
        * follow_followers.txt
        * follow_following.txt
        * like_hashtags.txt
        * like_users.txt
    and do the job. This bot can be run 24/7.
"""

import os
import sys
from random import shuffle

sys.path.append(os.path.join(sys.path[0], '../../'))
from instabot import Bot

bot = Bot()
bot.login()

print("Current script's schedule:")

competitors_list = bot.read_list_from_file("follow_followers.txt")
print("Going to follow followers of:", competitors_list)


random_users_list = []
for competitor in competitors_list:
    followers = bot.get_user_followers(competitor)
    if not followers:
        self.logger.info("{} not found / closed / has no followers.".format(user_id))
    else:

        #get 10% random selection from each user
        shuffle(followers)
        sizee = len(followers) % 10
        random_users_list.append(followers[:sizee])

bot.follow_users(random_users_list)
