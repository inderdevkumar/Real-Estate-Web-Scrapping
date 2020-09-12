
# Able to acces price for one real estate
import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c= r.content
soup= BeautifulSoup(c, "html.parser")
alll= soup.find_all("div", {"class":"propertyRow"})
#To remove new lines and spacesss we used replace
#To get text we used text

x= alll[0].find("h4", {"class": "propPrice"}).text.replace("\n","").replace(" ", "")
#x.replace("\n","").replace(" ", "")
print(x)