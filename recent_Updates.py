#@author Tucker Ferguson
#1/29/2020
#
# Step 1) Utilizing urllib3/BeautifulSoup I access a web address, extract its html, parse using bs4.
#
# Step 2) Using regular expressions (re) to extract headlines

from bs4 import BeautifulSoup
import urllib3
import re

#method for clean output
def pretty_output(formatter):
    for i,x in enumerate(formatter) :
        print("News Article {}): {}".format(i+1,x))

#handles re and stnd string methods for preparation of pretty_output()
def headline(newsInfo) :
    outputList = []
    formatter = []
    pattern = r"\">\w.+</a"
    for x in range(len(newsInfo) - 2):
        if x % 2 == 0: 
            output = re.search(pattern, str(newsInfo[x]))
            outputList.append(output.group(0))
    for entries in outputList :        
        if '\">' in entries :
            entries = entries.replace('\">',"")
        if '</a' in entries :
            entries = entries.replace('</a',"")
            formatter.append(entries)
    pretty_output(formatter)

#access website using urllib3, parse html tree using bs4
myPool = urllib3.PoolManager()
content = myPool.request('GET','https://oldschool.runescape.com/')
souped_Content = BeautifulSoup(content.data,"html.parser")
newsInfo = souped_Content.find_all("a",class_="secondary-link")

#soup is powerful but only to an extent now we leverage regular expressions
headline(newsInfo)
