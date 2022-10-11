import os
#imports the os module so that it can be used in this py file.
#basically os module is installed by default, you can check it or download it by pip-install-os.

shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")
#takes an input from the user and stores it in the variable named shutdown.
if shutdown == 'yes':
#checks if the input is yes.
 os.system("shutdown /s /t 1")
#if the input is yes, it will shutdown your system.

#os.shutdown(s = 0, m = 0, h = 0) explained
#s = time to wait before shutting down (in seconds), added to m and h
#m = time to wait before shutting down (in minutes), added to s and h
#h = time to wait before shutting down (in hours), added to s and m

elif shutdown == 'no':
#checks if the input given by the user is no.
    exit()
#if the input is no, then it will exit the code.
else:
    print("Please input a valid argument, either yes or no")
#if the input given by the user is neither yes or no, it will throw an error message.
