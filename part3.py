# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
michiganDailyUrl="https://www.michigandaily.com/"

def scrapper (url):

    page= requests.get(url)
    pagecontent= page.content
    soup= BeautifulSoup(pagecontent, 'html.parser')
    return soup


michigandailycontent = scrapper("https://www.michigandaily.com/")



print("Michigan Daily -- MOST READ")
mostReadDiv = michigandailycontent.find("div", attrs={'class' : 'view-most-read'}).find("ol").find_all("li")
for item in mostReadDiv:

    print(item.find("a").text.strip())

    try:
        linksoup =scrapper (michiganDailyUrl+item.find("a")['href'])
        author= linksoup.find("div", attrs = {"class" : "byline"}).find('div').find('a').text.strip()
        print("By " + author)
    except:
        linksoup =scrapper (michiganDailyUrl+item.find("a")['href'])
        author= linksoup.find("p", attrs = {"class" : "info"}).contents[0]
        print(author)
    # print ("\n")
