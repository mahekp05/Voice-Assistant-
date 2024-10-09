#pip install requests

import requests
from ss import *

#MAKE SURE YOU ARE USING RIGHT LINK HERE
api_address = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + api_key

#from requests module -- get list that has all latest news -- can print this variable to see entire list
json_data = requests.get(api_address).json()

#empty list to store news
news_list = []

def get_news():
    for i in range(3): #extract data from json file
        news_list.append("Number" + str(i+1) + " ," + json_data["articles"][i]["title"]+".")

    return news_list

#list = news()
#print(arr)
