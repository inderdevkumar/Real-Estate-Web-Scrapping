# To load extra features which are not visible but can be seen when clicked on the in deatils


import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c= r.content
soup= BeautifulSoup(c, "html.parser")
alll= soup.find_all("div", {"class":"propertyRow"})#  find_all is used beacuse there are many classs with propertRow, also can be used find_All  
#To remove new lines and spacesss we used replace
#To get text we used text
#length= len(alll)
for item in alll:
    print(item.find("h4", {"class", "propPrice"}).text.replace("\n","").replace(" ", "")) # For price
    print(item.find_all("span",{"class", "propAddressCollapse"})[0].text) # getting 1st address 
    print(item.find_all("span",{"class", "propAddressCollapse"})[1].text)  # Geting locality
    try:
        print(item.find("span", {"class","infoBed"}).find("b").text)  #This is to get text inside bold
    except:
        print(None)
    try:
        print(item.find("span", {"class","infoSqFt"}).find("b").text)  #This is to get text inside bold
    except:
        print(None)
    try:
        print(item.find("span", {"class","infoValueFullBath"}).find("b").text)  #This is to get text inside bold
    except:
        print(None)
    try:
        print(item.find("span", {"class","infoValueHalfBath"}).find("b").text)  #This is to get text inside bold
    except:
        print(None)
    
    for column_group in item.find_all("div", {"class": "columnGroup"}):
        #print(column_group)
        for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featuregroup"}), column_group.find_all("span", {"class": "featureName"})):
            print(feature_group.text, feature_name.text )


    print(" ")

