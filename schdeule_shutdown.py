import os

def shutdown(minutes):
    seconds = minutes * 60
    os.system(f'shutdown /s /t {seconds}')
    
minutes = int(input("Enter the number of minutes until shutdown: "))
shutdown(minutes)
