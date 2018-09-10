"""
    instabot example

    Workflow:
        Welcome message for new followers.
"""

import argparse
import os
import sys
from datetime import datetime, timedelta
from tqdm import tqdm
import time
sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot, utils
bot = Bot()

NOTIFIED_USERS_PATH = 'notified_users.txt'


parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
parser.add_argument('-users', type=str, nargs='?', help='a path to already notified users')
parser.add_argument('-message', type=str, nargs='?', help='message text')
args = parser.parse_args()


bot.login(username=args.u, password=args.p,
          proxy=args.proxy)
print("starting to run\n")

while 1:
    print ('Starting a fresh hourly run\n')

    # Check on existed file with notified users
    notified_users = utils.file(NOTIFIED_USERS_PATH)
    if not notified_users.list:
    	notified_users.save_list(bot.followers)
    	print(
            'All followers saved in file {users_path}.\n'
            'In a next time, for all new followers script will send messages.'.format(
            users_path=NOTIFIED_USERS_PATH
            )
        )   
        exit(0)

    print('Read saved list of notified users. Count: {count}'.format(
    count=len(notified_users)
    ))
    all_followers = bot.followers
    print('Amount of all followers is {count}'.format(
    count=len(all_followers)
    ))

    new_followers = set(all_followers) - notified_users.set

  
    if not new_followers:
        print("no new followers right now. This sucks! I'm going to sleep again\n")
	#sleepytiem
	#re-set the time
    	dt = datetime.now() + timedelta(hours=1)
    	dt = dt.replace(minute=10)
	pc = 0
    	while datetime.now() < dt:
	    pc += 1
            cur = int(str(datetime.now()).split(' ')[1][3:5])
            goal = int(str(dt).split(' ')[1][3:5])
            if cur < 10:
                t = 10 - cur
            else:
                t = 60 - cur
	    if pc is 10:
    	    	print("sleeping: will run again in " +str(t)+" minutes\n")
		pc = 0
	    time.sleep(1)
    
  
    print('Found new followers. Count: {count}'.format(
    count=len(new_followers)
    ))

    for follower in tqdm(new_followers):
        try:
            name = str(bot.get_user_info(follower)["full_name"])
            if len(name.split(' ')) is 2:
                name = name.split(' ')[0]
            
	
            MESSAGE = "Hey "+name+"! Thanks for checking out our eco-friendly, reusable stainless-steel straws! Our mission is to eliminate as much plastic as possible in order to preserve our oceans. Getting your own Boba Buddy is a simple way to eliminate up to 600 plastic straws that hurt marine wildlife everyday. If you're ready to join the movement, click on one of our pictures, or check out our website at thebobabuddy.com - You'll make a difference! Have an awesome day, and keep making smart choices for our planet <3"
        except:
            MESSAGE = "Hey there, thanks for checking out our eco-friendly, stainless-steel straws! Our mission is to eliminate as much plastic as possible in order to preserve our oceans, one straw at a time. Getting your own Boba Buddy is a simple way to eliminate up to 600 plastic straws that hurt marine wildlife everyday. If you're ready to join the movement, click on one of our pictures, or check out our website at thebobabuddy.com - You'll make a difference! Have a beautiful day, and keep making smart choices for our planet <3"

        
        print(MESSAGE)
	time.sleep(2)
        if bot.send_message(MESSAGE, follower):
            notified_users.append(follower)

    #re-set the time
    dt = datetime.now() + timedelta(hours=1)
    dt = dt.replace(minute=10)


