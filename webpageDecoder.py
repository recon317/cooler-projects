import requests
from bs4 import BeautifulSoup

#decoding NY Times Webpage to return all article titles


url = requests.get('https://www.nytimes.com/')  #request ny times home page

print(url.status_code) #if 200 code is printed then request is success
print()

soup = BeautifulSoup(url.content, 'html.parser')  #parses that page

for title in soup.find_all('h3'): #for loop for find_all list
    findAllSyntax = title.get_text() #converts items in list to text
    print(findAllSyntax) #prints out titles