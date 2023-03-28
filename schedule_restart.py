import os
import time

minutes = int(input("Enter the number of minutes to restart your PC: "))
seconds = minutes * 60

# delay the restart process for the specified time
time.sleep(seconds)

# restart the PC
os.system("shutdown /r /t 1")
