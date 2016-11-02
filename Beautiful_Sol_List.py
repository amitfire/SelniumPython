from bs4 import BeautifulSoup
import requests

url = raw_input("Please Enter the Url\n")
request = requests.get(url=url)
data = request.content
#print data
soup = BeautifulSoup(data)
for link in soup.find_all('a'):
    print link.text ,"--->" ,link.get('href')
laptops = soup.find_all("div",{"class": "_3wU53n"})
print laptops
for lap in laptops:
    print lap.contents

#print soup.prettify()

# try:
#     print data
# except UnicodeEncodeError as e:
#     print e








