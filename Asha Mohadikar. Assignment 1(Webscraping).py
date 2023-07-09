#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ASSIGNMENT 1


# In[ ]:


WEB SCRAPING


# In[ ]:


1) Write a python program to display all the header tags from wikipedia.org and make data frame.


# In[8]:


from bs4 import BeautifulSoup
import requests


# In[10]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[241]:


page


# In[ ]:


Page Content


# In[12]:


soup = BeautifulSoup(page.content)
soup


# In[34]:


first_title = soup.find('span',class_="mw-headline")
first_title


# In[35]:


first_title.text


# In[40]:


header_tags = []

for i in soup.find_all('span',class_="mw-headline"):
    header_tags.append(i.text)
    

header_tags


# In[128]:


import pandas as pd
df = pd.DataFrame({'header_tags':header_tags})
print(df)


# In[ ]:





# In[ ]:


2) Write a python program to display list of respected former presidents of India(i.e. Name , Term ofoffice)
from https://presidentofindia.nic.in/former-presidents.htm and make data frame.


# In[47]:


from bs4 import BeautifulSoup
import requests


# In[64]:


page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')


# In[49]:


page


# In[ ]:


Page Content


# In[51]:


soup = BeautifulSoup(page.content)
soup


# In[52]:


first_title = soup.find('div',class_="presidentListing")
first_title


# In[53]:


first_title.text


# In[54]:


Titles = []

for i in soup.find_all('div',class_="presidentListing"):
     Titles.append(i.text)
    

Titles


# In[60]:


import pandas as pd
df = pd.DataFrame({'Titles':Titles})
print(df)


# In[ ]:





# In[ ]:


3) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
b) Top 10 ODI Batsmen along with the records of their team andrating.
c) Top 10 ODI bowlers along with the records of their team andrating.


# In[ ]:


a)


# In[65]:


from bs4 import BeautifulSoup
import requests


# In[263]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/test')
page


# In[264]:


soup = BeautifulSoup(page.content)
soup


# In[265]:


table = soup.find('table',class_="table")
table


# In[266]:


table.text


# In[267]:


teams = []
matches = []
points = []
ratings = []

for i in soup.find_all('table',class_="table"):
     teams= i.find_all('span', class_='u-hide-phablet')
     matches= i.find_all('td')
     points = i.find_all('td')
     ratings = i.find_all('td')
     teams.append(i.text)
     matches.append(i.text)
     points.append(i.text)
     ratings.append(i.text)
    

teams
matches
points
ratings


# In[ ]:


import pandas as pd
   
df = pd.DataFrame({'teams':teams,'matches':matches,'points':points,'ratings':ratings})
df.index += 1:
    
print(df)


# In[ ]:





# In[ ]:





# In[ ]:


b)


# In[156]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/test')
page


# In[157]:


soup = BeautifulSoup(page.content)
soup


# In[158]:


table = soup.find('tr',class_=('rankings-block__banner','table-body'))
table


# In[159]:


table.text


# In[160]:


req=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
soup=BeautifulSoup(req.content)
player=soup.find_all('tr',class_=('rankings-block__banner','table-body'))
top10=player[0:10]
data={'Player_Name':[],'Team_Name': [], 'Rating':[]}
for i in top10:
    bat=i.find_all('td',recursive=True)
    data['Player_Name'].append(bat[1].text.replace('\n',''))
    data['Team_Name'].append(bat[2].text.replace('\n',''))
    data['Rating'].append(bat[3].text.replace('\n',''))
ODIBATSMAN=pd.DataFrame(data,index=range(1,11))
ODIBATSMAN


# In[ ]:


c)


# In[162]:


req=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
soup=BeautifulSoup(req.content)
bowler=soup.find_all('tr',class_=('rankings-block__banner','table-body'))
Top10=bowler[0:10]
bdata={'Player_Name':[],'Team_Name': [], 'Rating':[]}
for i in Top10:
    bat=i.find_all('td',recursive=True)
    bdata['Player_Name'].append(bat[1].text.replace('\n',''))
    bdata['Team_Name'].append(bat[2].text.replace('\n',''))
    bdata['Rating'].append(bat[3].text.replace('\n',''))
ODIBOWL=pd.DataFrame(bdata,index=range(1,11))
ODIBOWL


# In[ ]:





# In[ ]:


4) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
b) Top 10 women’s ODI Batting players along with the records of their team and rating.
c) Top 10 women’s ODI all-rounder along with the records of their team and rating.


# In[ ]:


a)


# In[ ]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')


# In[163]:


page


# In[165]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
req=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
soup=BeautifulSoup(req.content)
team=soup.find_all('tr',class_=('rankings-block__banner','table-body'))
top10=team[0:10]
data = {'Team_Name':[],'Matches': [],'Points': [],'Rating':[]}

for i in top10:
    pnt=i.find_all('td',recursive=True)
    data['Team_Name'].append(i.find('span',class_='u-hide-phablet').text)
    data['Matches'].append(pnt[2].text)
    data['Points'].append(pnt[3].text)
    data['Rating'].append(pnt[4].text.strip().replace('\n',''))
WomenTeam=pd.DataFrame(data,index=range(1,11))
WomenTeam


# In[ ]:


b)


# In[166]:


req=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
soup=BeautifulSoup(req.content)
player=soup.find_all('tr',class_=('rankings-block__banner','table-body'))

top10=player[0:10]
data={'Player_Name':[],'Team_Name': [], 'Rating':[]}

for i in top10:
    bat=i.find_all('td',recursive=True)
    data['Player_Name'].append(bat[1].text.replace('\n',''))
    data['Team_Name'].append(bat[2].text.replace('\n',''))
    data['Rating'].append(bat[3].text.replace('\n',''))
BATW=pd.DataFrame(data,index=range(1,11))  
BATW


# In[ ]:


c)


# In[167]:


req=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
soup=BeautifulSoup(req.content)
player=soup.find_all('tr',class_=('rankings-block__banner','table-body'))

top10=player[0:10]
data={'Player_Name':[],'Team_Name': [], 'Rating':[]}

for i in top10:
    bat=i.find_all('td',recursive=True)
    data['Player_Name'].append(bat[1].text.replace('\n',''))
    data['Team_Name'].append(bat[2].text.replace('\n',''))
    data['Rating'].append(bat[3].text.replace('\n',''))
W_All=pd.DataFrame(data,index=range(1,11))
W_All


# In[ ]:





# In[ ]:


5) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and
make data frame
i) Headline
ii) Time
iii) News Link


# In[ ]:


a)


# In[97]:


from bs4 import BeautifulSoup
import requests


# In[98]:


page = requests.get('https://www.cnbc.com/world/?region=world')


# In[99]:


page


# In[173]:


import requests
from bs4 import BeautifulSoup
page=requests.get('https://www.cnbc.com/world/?region=world')
page
news=BeautifulSoup(page.content)
news
# Headline
Headline=[]
for i in news.find_all('div',class_='RiverHeadline-headline RiverHeadline-hasThumbnail'):
   Headline.append(i.text)
Headline


# In[175]:


import pandas as pd
df = pd.DataFrame({'Headline':Headline})
print(df)


# In[ ]:


b)


# In[174]:


# Time
Time=news.find('time')
Time
Time.text
Time=[]
for i in news.find_all('time'):
   Time.append(i.text)
Time


# In[176]:


import pandas as pd
df = pd.DataFrame({'Time':Time})
print(df)


# In[ ]:


c)


# In[182]:


# Newslink
url = "https://www.cnbc.com/world/?region=world"
webpage = requests.get(url) 
link = BeautifulSoup(webpage.content, "html.parser")
for link in trav.find_all('a'):
    print(type(link), " ", link)
link.text


# In[ ]:


import pandas as pd
  df = pd.DataFrame({'url':url})
  df.index += 1:
    
print(df)


# In[ ]:





# In[ ]:





# In[ ]:


6) Write a python program to scrape the details of most downloaded articles from AI in last 90
days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
Scrape below mentioned details and make data frame
i) Paper Title
ii) Authors
iii) Published Date
iv) Paper URL


# In[186]:


page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page


# In[187]:


soup = BeautifulSoup(page.content)
soup


# In[188]:


first_title = soup.find('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg")
first_title


# In[189]:


first_title.text


# In[190]:


Paper_Title = []

for i in soup.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    Paper_Title.append(i.text)
    

Paper_Title


# In[191]:


import pandas as pd
df = pd.DataFrame({'Paper_Title':Paper_Title})
print(df)


# In[ ]:


b)


# In[192]:


first_title = soup.find('span',class_="sc-1w3fpd7-0 dnCnAO")
first_title


# In[193]:


first_title.text


# In[194]:


Authors = []

for i in soup.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    Authors.append(i.text)
    

Authors


# In[195]:


import pandas as pd
df = pd.DataFrame({'Authors':Authors})
print(df)


# In[197]:


first_title = soup.find('span',class_="sc-1thf9ly-2 dvggWt")
first_title


# In[198]:


first_title.text


# In[199]:


Published_Date = []

for i in soup.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    Published_Date.append(i.text)
    

Published_Date


# In[200]:


import pandas as pd
df = pd.DataFrame({'Published_Date':Published_Date})
print(df)


# In[ ]:


url = []

for i in soup.find_all('a',class_='pod-listing__title')['href']:
    url.append(i.text)
    

url


# In[ ]:





# In[ ]:


7) Write a python program to scrape mentioned details from dineout.co.inand make data frame
i) Restaurant name
ii) Cuisine
iii) Location
iv) Ratings
v) Image UR


# In[ ]:


i)


# In[219]:


page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page


# In[220]:


soup = BeautifulSoup(page.content)
soup


# In[221]:


first_title = soup.find('a',class_="restnt-name ellipsis")
first_title


# In[222]:


first_title.text


# In[223]:


Restaurant_Name = []

for i in soup.find_all('a',class_="restnt-name ellipsis"):
    Restaurant_Name.append(i.text)
    

Restaurant_Name


# In[224]:


import pandas as pd
df = pd.DataFrame({'Restaurant_Name':Restaurant_Name})
print(df)


# In[ ]:


ii)


# In[225]:


# Cusines
price=[]
for i in soup.find_all('span',class_="double-line-ellipsis"):
    price.append(i.text)
price


# In[227]:


import pandas as pd
df = pd.DataFrame({'price':price})
print(df)


# In[ ]:


iii)


# In[228]:


# Location
location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
location


# In[229]:


import pandas as pd
df = pd.DataFrame({'loction':location})
print(df)


# In[ ]:


iv)


# In[230]:


# Ratings
Ratings=[]
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    Ratings.append(i.text)
Ratings


# In[231]:


import pandas as pd
df = pd.DataFrame({'Ratings':Ratings})
print(df)


# In[ ]:


v)


# In[232]:


# Images
images=[]
for i in soup.find_all('img',class_="no-img"):
    images.append(i['data-src'])
images


# In[233]:


import pandas as pd
df = pd.DataFrame({'images':images})
print(df)


# In[234]:


import pandas as pd
df = pd.DataFrame({'Restaurant_Name':Restaurant_Name,'price':price,'loction':location,'Ratings':Ratings,'images':images})
print(df)


# In[ ]:




