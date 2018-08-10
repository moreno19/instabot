"""
    instabot example

    Dependencies:
        You must have a file with comments to post.
        The file should have one comment per line.

    Notes:
        You can change file and add there your comments.
"""

import sys
import os

sys.path.append(os.path.join(sys.path[0], '../../'))
from instabot import Bot


if len(sys.argv) < 3:
    print("USAGE: Pass a path to the file with comments and an hastag to comment")
    print("Example: %s comments_emoji.txt dog cat" % sys.argv[0])
    exit()

hashtags = ["turtle", "savetheturtles", "boba", "bubbletea", "vegansmoothie", "smoothie", "strawssuck", "plasticpollutes", "beachcleanup", "ecoresort", "yerbamate", "tealeaves"]
categories = ["turtle", "tea", "smoothie", "boba", "beach", "plasticstraws"]
#turtle
comments_file_name_1 = "turtlecomments.txt"


#tea
comments_file_name_1 = "teacomments.txt"

#smoothie
comments_file_name_1 = "smoothiecomments.txt"


#boba
comments_file_name_1 = "bobacomments.txt"


#beach
comments_file_name_1 = "beachresortcomments.txt"


#plasticstraws
comments_file_name_1 = "strawcomments.txt"


comments_file_name = sys.argv[1]
hashtags = sys.argv[2:]
if not os.path.exists(comments_file_name):
    print("Can't find '%s' file." % comments_file_name)
    exit()


bot = Bot(comments_file=comments_file_name)
bot.login()
for hashtag in hashtags:
    bot.comment_hashtag(hashtag)
bot.logout()
