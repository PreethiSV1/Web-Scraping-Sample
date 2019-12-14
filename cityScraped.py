# importing requests library to send HTTP requests 
import requests

# Web Scraper tool BeautifulSoup
from bs4 import BeautifulSoup

# importing pandas for data alignment and analysis
import pandas

#requests.get(url).text will fetch a website and returns the HTML text of the website.
website_url = requests.get("https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population").text

soup = BeautifulSoup(website_url,"lxml")

#prettify method to turn a BS parse tree into a nicely formatted unicode string
soup.prettify()

# finding the required table by going through the HTML
wikiTable = soup.findAll('table',{'class':'wikitable sortable'})

# print(len(wikiTable)) 
# Outputs 12 because there are 12 such 'wikitable sortable' tables in the webpage each holding 25 ranks.

# wikiTable[0] selects the table of top 1-25 cities 
rows = wikiTable[0].findAll('tr')

# Finding all cities names from the first link in each row
City = []
for j in rows:
	# To find the first element by tag, we use the BeautifulSoup object's find() method, 
	# which takes a tag's name as the first argument
    dummyLink = j.find('a')
    if  dummyLink!= None:
        City.append(dummyLink.text)
City = City[1:]

# scraping the rank, population, state of each city from each row
Rank = []
CityPopulation11= []
CityPopulation01= []  
State = []
for j in rows:
	# findAll() method returns the list of all tags with the argument name
    dummy = j.findAll('td')
    if  dummy!= []:
        rank = dummy[0].text
        # used to remove extra new line escape sequence
        if rank[-1] == '\n':
            rank = rank[:-1]
        Rank.append(rank)
        
        city11 = dummy[2].text
        if city11[-1] == '\n':
            city11 = city11[:-1]
        CityPopulation11.append(city11)
        
        city01 = dummy[3].text
        if city01[-1] == '\n':
            city01 = city01[:-1]
        CityPopulation01.append(city01)
        
        state = dummy[4].text
        if state[-1] == '\n':
            state = state[:-1]
        State.append(state)

# each of the following prints a list
print(Rank)
print(City)
print(CityPopulation11)
print(CityPopulation01)
print(State)

# creating a dataframe to align these data into table using columns
df = pandas.DataFrame()

# Adding data into data frame and setting up the column name
df['Rank'] = Rank
df['City'] = City
df['Population 2011'] = CityPopulation11
df['Population 2001'] = CityPopulation01
df['State (or UT)'] = State

print()
print("List of top 25 Indian cities by population\n\n".center(80))
print(df)
