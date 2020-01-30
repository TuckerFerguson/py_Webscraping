#@author Tucker Ferguson
#1/29/2020
#
# Step 1) Utilizing urllib3/BeautifulSoup I access a web address, extract its html, parse using bs4.
#
# Step 2) Using regular expressions (re) to extract the active player count 

import urllib3
from bs4 import BeautifulSoup
import re
import time

html_Pool = urllib3.PoolManager()
count = 1
print("""
✝ Utilizing urllib3 to fetch webpage: "www.oldschool.runescape"
* Using BeautifulSoup to traverse html and grab data
* Enjoy!     
""")
#outputs active player count 
def sleeper(number_Active):
    global count
    t = time.localtime()
    currentTime = time.strftime("%H:%M:%S", t)
    print("{}) Active Players: {} at {}\n".format(count, number_Active,currentTime))
    count += 1

#arbitrary range 10 using time module to delay consecutive scrapes (2 sec)
for i in range(5):
    time.sleep(2)
#Using oldschool runescapes homepage to pull data
    url = html_Pool.request('GET',"https://oldschool.runescape.com/")
    soup = BeautifulSoup(url.data, 'html.parser')
    playerCount = soup.find_all("p",class_="player-count")
    playerCount = str(playerCount)
    pattern = r">\w.+<"
    playerCount = re.search(pattern,playerCount)
    giveMe_Num = playerCount.group(0)
#for formatting purpose number_Active is string   
    number_Active = ""
    for i in range(len(giveMe_Num)) :
        if giveMe_Num[i].isdigit():
            number_Active += str(giveMe_Num[i])
    sleeper(number_Active)
