import requests

#Test.py is for testing the rest apis. we can call api basically.
BASE = "http://127.0.0.1:5000/"

#sending the get request to base url + helloworld
response = requests.get(BASE + "helloworld")
print(response.json())