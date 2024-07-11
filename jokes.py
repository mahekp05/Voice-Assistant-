import requests
#official joke api

#store api adress
url = "https://official-joke-api.appspot.com/random_joke"

#convert url to json -- request to get url then covert
json_data = requests.get(url).json()

#list with two empty strings -- first setup, second punchline
arr = ["",""]
arr[0] = json_data["setup"]
arr[1] = json_data["punchline"]
def joke():
    return arr 

#when you refresh page, the joke changes