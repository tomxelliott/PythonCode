import urllib2
from bs4 import BeautifulSoup
import pandas as pd # need to import anaconda to use this API

# specify the url
wiki = "https://en.wikipedia.org/wiki/Tom_Brady"

# Query the website and return the html to the variable 'page'
page = urllib2.urlopen(wiki)

# import the Beautiful Soup functions to parse the data returned from the website


soup = BeautifulSoup(page)

print soup.prettify()

print soup.title

print soup.script.string

print soup.a

print soup.find_all("a")

right_table = soup.find('table', { "class" : 'wikitable sortable'})

#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states = row.findAll('th') #to store second column data
    if len(cells)==6:
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))



df = pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
df
