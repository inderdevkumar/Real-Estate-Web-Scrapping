# To load extra features which are not visible but can be seen when clicked on the in deatils


import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c= r.content
soup= BeautifulSoup(c, "html.parser")
alll= soup.find_all("div", {"class":"propertyRow"})#  find_all is used beacuse there are many classs with propertRow, also can be used find_All  
#To remove new lines and spacesss we used replace
#To get text we used text
#length= len(alll)
l= [] #Creating emty list to story dictionary and finallyy convert in dataframe than to csv
page_nr= soup.find_all("a", {"class", "Page"})[-1].text
base = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

for page in range(0, 30, 10):
    #r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/"+str(page)+"&subView= searchView.Paginate")
    #r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/#t=0&s=0"+str(page))
    #c= r.json()["list"]
    r = requests.get(base+str(page))
    c= r.content
    soup= BeautifulSoup(c, "html.parser")
    alll= soup.find_all("div", {"class":"propertyRow"})

    for item in alll:
        d= {}# Creating empty dictionary
        d["Price"]= item.find("h4", {"class", "propPrice"}).text.replace("\n","").replace(" ", "") # For price
        d["Address"]= item.find_all("span",{"class", "propAddressCollapse"})[0].text # getting 1st address 
        d["Locality"]= item.find_all("span",{"class", "propAddressCollapse"})[1].text  # Geting locality
        try:
            d["Beds"]= item.find("span", {"class","infoBed"}).find("b").text  #This is to get text inside bold
        except:
            d["Beds"]= None
        try:
            d["Area"]= item.find("span", {"class","infoSqFt"}).find("b").text  #This is to get text inside bold
        except:
            d["Area"]= None
        try:
            d["Full_Bath"]= item.find("span", {"class","infoValueFullBath"}).find("b").text  #This is to get text inside bold
        except:
            d["Full_Bath"]= None
        try:
            d["Half_Bath"]= item.find("span", {"class","infoValueHalfBath"}).find("b").text  #This is to get text inside bold
        except:
            d["Half_Bath"]= None
        
        for column_group in item.find_all("div", {"class": "columnGroup"}):
            #print(column_group)
            for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featuregroup"}), column_group.find_all("span", {"class": "featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Extra_Feature"]= feature_name.text


        l.append(d)

df= pd.DataFrame(l)
df.to_excel("Real_estate_web_scrapped_data.xlsx")
