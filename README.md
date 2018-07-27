# Instabot


DO NOT pip install custom module inside of the folder, will create redundancies
*pip install -e git+http://github.com/moreno19/instabot2.gi#egg=instabot2*
run this at the same level as your overall directory, will create new /src folder, make sure your repo is up to date
this is specifically for bot.____ files

usually, just run target_competitiors.py -> this find the follow_followers.txt list, gets their latest post, and likes and follows a portion of those users
-safe, might have to adjust like and follow latency

or, run specify_competitors.py -> same script as above, but use if you want to focus on 2 or 3 competitiors, input is through the command line
- python specify_competitors.py -users berniesanders

unfollow_non_followers.py is self explanatory
unfollow_everyone takes into account whitelists, might work too




Instagram apparently limits api calls to 200 per hour. This implies two modes
1. follow and like - 30 second latency
2. unfollow only - 14 second latency

DISREGARD ABOVE. 
new gameplan is to like and follow using like_your_last_media_likers.py
delete using unfollow_followers.py
once a day message everyone using welcome_message.py

add new targets to follow_followers.txt -> will target their fans

---
### [Read the Docs](https://instagrambot.github.io/docs/) | [Contribute](https://github.com/instagrambot/docs/blob/master/CONTRIBUTING.md)
---

[![Telegram Chat](https://img.shields.io/badge/chat%20on-Telegram-blue.svg)](https://t.me/instabotproject)
![Python 2.7, 3.5, 3.6](https://img.shields.io/badge/python-2.7%2C%203.5%2C%203.6-blue.svg)
[![PyPI version](https://badge.fury.io/py/instabot.svg)](https://badge.fury.io/py/instabot)
[![Build Status](https://travis-ci.org/instagrambot/instabot.svg?branch=master)](https://travis-ci.org/instagrambot/instabot)
[![codecov](https://codecov.io/gh/instagrambot/instabot/branch/master/graph/badge.svg)](https://codecov.io/gh/instagrambot/instabot)
<span class="badge-bitcoin"><a href="https://github.com/instagrambot/instabot/blob/master/.github/DONATE_BITCOIN.md" title="Donate once-off to this project using Bitcoin"><img src="https://img.shields.io/badge/bitcoin-donate-yellow.svg" alt="Bitcoin donate button" /></a></span>

### Installation
Install `instabot` with:
```
pip install -U instabot
```
#### or see [this](https://instagrambot.github.io/docs/en/#installation) for more details.



![Instabot is better than other open-source bots!](https://github.com/instagrambot/docs/blob/master/img/instabot_3_bots.png "Instabot is better than other open-source bots!")
