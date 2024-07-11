#pip install requests 

import requests 
from ss import *

api_adress = "https://newsapi.org/v2/everything?q=keyword&apiKey=" + api_key

#from requests module
json_data = requests. get(api_adress).json() #list that has all the latest news

ar = [] #empty list to store news

def news():
    for i in range(3): #extract data from json file
        ar.append("Number" + str(i+1) + " ," + json_data["articles"][i]["title"]+".")

    return ar


#arr = news()
#print(arr)