import os
import subprocess

def switchup():
    f = open("choice.txt", "r")
    num = int(f.read()[0])
    f.close()

    f = open("choice.txt", "w")
    if num is not 6:
        num += 1
        f.write(str(num))
    else:
        num = 0
        f.write(str(num))
    f.close()
    return num


f = open("choice.txt", "r")
choice = int(f.read()[0])

while(1):
    if choice is 0:
        choice = switchup()
        subprocess.call(["python","comment_hashtags.py","turtlecomments.txt", "turtle", "savetheturtles"])

    if choice is 1:
        choice = switchup()
        subprocess.call(["python","comment_hashtags.py","bobacomments.txt", "boba", "bubbletea"])

    if choice is 2:
        choice = switchup()
        subprocess.call(["python","comment_hashtags.py","smoothiecomments.txt", "vegansmoothie", "smoothie"])

    if choice is 3:
        choice = switchup()
        subprocess.call(["python","comment_hashtags.py","strawcomments.txt", "strawssuck", "plasticpollutes"])

    if choice is 4:
        choice = switchup()
        subprocess.call(["python","comment_hashtags.py","beachresortcomments.txt", "beachcleanup", "ecoresort"])

    if choice is 5:
        choice = switchup()
        subprocess.call(["python","comment_hashtags.py","teacomments.txt", "tea", "yerbamate", "tealeaves"])
    if choice is 6:
        choice = switchup()