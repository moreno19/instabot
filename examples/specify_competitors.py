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

def random_subset( iterator, K ):
    result = []
    N = 0

    for item in iterator:
        N += 1
        if len( result ) < K:
            result.append( item )
        else:
            s = int(random.random() * N)
            if s < K:
                result[ s ] = item

    return result



parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
parser.add_argument('users', type=str, nargs='+', help='users')
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)



competitors_list = [x for x in args.users]
likers = []
master_user_list = []
numcomp = len(competitors_list)
cnt = 0
for username in competitors_list:
    cnt+=1
    print(str(cnt) +" out of "+str(numcomp)+"competitors, getting first picture\n")
    

    medias = bot.get_user_medias(username, filtration=False)

    if len(medias):
        
        likers = bot.get_media_likers(medias[0])


        #at most, pick 400 users from each person if targeting 2 competitors -> 800per day/ 2 competitiors = 400 users each, etc
        if len(likers) > 800/len(args.users):
            likers = random_subset(likers, 800/len(args.users))

        master_user_list += likers
        print("likers for 1st pic of "+str(cnt)+"/"+str(numcomp)+"user added to masterlist of users\n\n")
    else:
        print("this account has no pics")

people = random_subset(master_user_list, len(master_user_list))
for person in tqdm(people):
    bot.like_user(person, amount=2)

    #only follow 10k+ follow accounts or 30% of users, like all the rest
    if bot.get_user_info(person, use_cache=False)["follower_count"] > 20000:
        bot.follow(person)

        with open("whitelist.txt", "a") as f:
            user_info = bot.get_user_info(bot.get_username_from_user_id(person))
            print(user_info["username"])
            print(user_info["full_name"])

            f.write(str(bot.get_username_from_user_id(person)) + "\n")
            print("ADDED to Whitelist.\r")

        with open("influencers.txt", "a") as g:
            g.write(str(bot.get_username_from_user_id(person)) + "\n")
            print("Potential Influencer found.\r")

        

    elif random.randint(1,11) <= 3:
        print("Attempting to follow this account")
        bot.follow(person)

f.close()
g.close()