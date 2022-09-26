from plyer import notification
import time


def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=5,
    )


nk = 0


while (True):
    print("upr wala ", nk)
    s = {}
    s[1] = "none"
    f = open("notification.txt", "r")
    s = f.readlines()
    print(int(s[0]))
    time.sleep(1)
    if (int(s[0]) == 1):
        f.close()
        nk = 1
        notifyme("EYE SAVER", "It's break time! Take a break of atleast 20 seconds")
        time.sleep(1200)
        print("ander wala ", nk)

    elif (int(s[0]) == 0):
        if (nk == 1):
            print("last", nk)
            break
