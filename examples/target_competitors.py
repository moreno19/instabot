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
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)


'''
select targeting option
'''
options = ['general list of related competitors/pages', 'boba places in nyc']
print("Choose target list:")
for idx, element in enumerate(options):
    print("{}) {}".format(idx+1,element))
i = input("Enter number: ")

try:
    if 0 < int(i) <= len(options):
            if int(i) is 1:
                competitors_list = bot.read_list_from_file("follow_followers.txt")
                self.logger.info("using the general list")
                master_user_list = []
                numcomp = len(competitors_list)
                cnt = 1

            elif int(i) is 2:
               competitors_list = bot.read_list_from_file("bobanyc.txt")
               self.logger.info("using the boba nyc list")
               master_user_list = []
               numcomp = len(competitors_list)
               cnt = 1

            
except:
    competitors_list = bot.read_list_from_file("follow_followers.txt")
    print("using the general list - EXCEPT")
    numcomp = len(competitors_list)
    cnt = 1
    i = 1
    master_user_list = []



if int(i) is 2 or int(i) is 1:
    for username in competitors_list:
        print(str(cnt) +" out of "+str(numcomp)+" competitors, getting first picture\n")
        cnt+=1

        medias = bot.get_user_medias(username, filtration=False)
        if len(medias):

            likers = bot.get_media_likers(medias[0])

            #at most, pick 50 users from each person
            if len(likers) > int(800/len(competitors_list)):
                likers = random_subset(likers, int(800/len(competitors_list)))

            master_user_list += likers
            print("likers for 1st pic added to masterlist of users\n\n")
        else:
            print("this account has no pics")

    master_user_list = random_subset(master_user_list, len(master_user_list)) #randomize order of list

    for person in tqdm(master_user_list):
        #person is an ID
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
