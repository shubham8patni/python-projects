# basic concept is string concatenation

# youtuber = "Shubham Patni" # is a string variable
# a few ways to do this
# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")

import random

choice = ""
mads = ['madlibs1', 'madlibs2'] #, 'madlibs3', 'madlibs4']
choice = random.choice(mads)

if choice == 'madlibs1':
    adj1 = input("adjective1: ")
    verb1 = input("verb1: ")
    verb2 = input("verb2: ")
    adj2 = input("adjective2: ")

    madlibs = f"Python programming is so {adj1}! It makes me excited all the time because I love to {verb1}. Because of Python {verb2} Machine learning and Deep Learning models has become very {adj2}!"
elif choice == 'madlibs2':
    verb = input("verb: ")
    famous_person = input("famous_person: ")
    
    madlibs = f"May the {verb} be with you. - {famous_person}"

print(madlibs)