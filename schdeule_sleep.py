import os
import time

minutes = int(input("Enter the number of minutes after which you want your computer to sleep: "))
seconds = minutes * 60

time.sleep(seconds)

os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
