'''
target: 16,000
hit target: 10
'''

import argparse
import os
import sys
import csv
from instabot import Bot, utils
from tqdm import tqdm

sys.path.append(os.path.join(sys.path[0], '../'))

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)


all_users_set = set()
emails = []
count = 0

hashtag_list = bot.read_list_from_file("hashtags_to_scrape.txt")
for hashtag in hashtag_list:
    all_users_set |= set(bot.get_hashtag_users(hashtag))


prominent_users = bot.read_list_from_file("users_to_scrape.txt")
for prominent_user in prominent_users:
	all_users_set |= set(bot.get_user_followers(prominent_user))

#setup csv
emailsfile = open("emails.csv", 'wb')

for person in tqdm(all_users_set):

	try:
		email = str(bot.get_user_info(person)["email"])
		count += 1
		print("email #"+count+": "+email)
		emails.append(email)
		#write to CSV
		f = csv.writer(emailsfile, dialect='excel')
		f.writerows(emails)
	except:
		print("this one didn't have an email \n")
	
	

	

emailsfile.close()







