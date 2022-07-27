from socket import timeout
from plyer import notification
import time
import sys

def notifyme(title , message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 5,
    )
'''    
while(True):
    s = {}
    s[1] = "none"
    f = open("d:\\nikhil python\\eye saver\\notification.txt","r")
    s = f.readlines()   
    print(int(s[0])) 
    time.sleep(1)
    if(int(s[0]) == 1):
        f.close()
        notifyme("or bhai" , "break bhi le le")    
        time.sleep(15)
        if(int(s[0]) == 0):
            sys.exit()'''

notifyme("Break bhi le" , "bhai yaa jaanu break le lo")    
time.sleep(5)            