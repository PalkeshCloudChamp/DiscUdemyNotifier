# importing the required libraries.

import time
import hashlib
from typing import cast
from urllib.request import urlopen,Request
from notifier import DiscUdemyNotification
# Setting the url you want to monitor

url = Request("https://www.discudemy.com/" , headers={'User-Agent' : 'Chrome'})
url2 = Request("https://www.discudemy.com/")
print("Url2:- " , url2)
print("Url:- ",url)

# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("running....")
time.sleep(10)
while True:
    try:
        # perform the get request and store it in a var
        response = urlopen(url).read()
        currentHash = hashlib.sha224(response).hexdigest()
        time.sleep(30)
        newHash = hashlib.sha224(response).hexdigest()
        if(currentHash == newHash):
            # print("same as earlier....")
            continue
        else:
            print("Something new happen......")
            DiscUdemyNotification()


            # again read the url/website
            response = urlopen(url).read()

            currentHash = hashlib.sha224(response).hexdigest()
            time.sleep(30)
            continue
    except Exception as e:
        print("Some Error..")