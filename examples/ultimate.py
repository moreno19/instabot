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

sys.path.append(os.path.join(sys.path[0], '../../'))
from instabot import Bot

bot = Bot()
bot.login()

print("Current script's schedule:")

follow_followers_list = bot.read_list_from_file("follow_followers.txt")
print("Going to follow followers of:", follow_followers_list)



tasks_list = []
for item in follow_followers_list:
    tasks_list.append((bot.follow_followers, {'user_id': item, 'nfollows': None}))



# shuffle(tasks_list)
for func, arg in tasks_list:
    func(**arg)
