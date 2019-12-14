# Web Scraping
Scrape data using BeautifulSoup from the website "https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
<br>
Web Scraping (also termed Screen Scraping, Web Data Extraction, Web Harvesting etc.) is a technique employed to extract large amounts of data from websites whereby the data is extracted and may be saved to a local file in your computer or to a database in table (spreadsheet) format.

The project’s objective is to scrape data using BeautifulSoup from the website "https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population" and to display data of top 25 cities by population in India in an aligned manner using Pandas data frames.

Data displayed by most websites can only be viewed using a web browser. They do not offer the functionality to save a copy of this data for personal use. The only option then is to manually copy and paste the data - a very tedious job which can take many hours or sometimes days to complete. Web Scraping is the technique of automating this process, so that instead of manually copying the data from websites, the Web Scraping software will perform the same task within a fraction of the time.

While there are various techniques that can be used to scrape the web, we use html parser to extract the data. Some other options for web scraping are using API and text-pattern matching using regular expressions.

## Processes involved in Web Scraping 
Web scraping a web page involves fetching it and extracting from it. Fetching is the downloading of a page (which a browser does when you view the page), which is done by using requests, a third-party HTTP library for Python.

After fetching the HTML content, we are left with the task of parsing the data. Since most of the HTML data is nested, we cannot extract data simply through string processing. Hence a parser is used, which can create a nested/tree structure of the HTML data.There are many HTML parser libraries available one among them is lxml, a third party Python parser.

We need to navigate and search the parse tree that we created, i.e. tree traversal. For this task, we will be using another third-party Python library, Beautiful Soup, for pulling data out of HTML and XML files. The data extracted is aligned using Pandas DataFrames.
 
## New Concepts Learned 
### Requests - Python Library
#### Used to make HTTP requests (under internet connection)
```
import requests
website = requests.get(“https://www.google.com”)
```
### BeautifulSoup - Python Library for Web Scraping 
#### Making the soup 
```
from bs4 import BeautifulSoup
soup = BeautifulSoup(“<html>data</html>")
```
#### Prettify the soup - to turn a BS parse tree into a nicely formatted unicode string
```
soup.prettify()
```
#### Find the first occurrence of a tag or find all of the tag’s occurrences, findAll() or find_all() returns all the tags and strings that match your filters.
```
soup.find(id=“link3")
soup.find_all('a')
```
### Pandas - DataFrames (used only for alignment in this project) 
#### Create Data Frame and add data and column names
```
df = pandas.DataFrame() 
df['ColumnName'] = ColumnValueList
```

## References
1. https://pypi.org/project/requests/2.11.1/
2. https://beautiful-soup-4.readthedocs.io/en/latest/
3. https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm 
4. https://medium.com/analytics-vidhya/web-scraping-wiki-tables-using-beautifulsoup-and-python-6b9ea26d8722
