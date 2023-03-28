import os

# get input from user for number of minutes
minutes = int(input("Enter the number of minutes after which you want to log out: "))

# convert minutes to seconds
seconds = minutes * 60

# log out the user after the specified time
os.system("shutdown -l -t {}".format(seconds))
