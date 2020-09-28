import requests

#Test.py is for testing the rest apis. we can call api basically.
BASE = "http://127.0.0.1:5000/"

#sending the get request to base url + helloworld
response = requests.put(BASE + "video/1", {"name":"sarang","views":30,"likes":10}) #passing request json for testing 
print(response.json())