import requests
import datetime as dt
from dotenv import dotenv_values

config = dotenv_values(".env")

URL = config["URL"]
GRAPH = config["GRAPH"]
TOKEN = config["TOKEN"]
USER = config["USER"]
G_ID= config["G_ID"]

#1 create USER

req = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#
# data = requests.post(URL, json=req)

#2 create graph

head = {
    "X-USER-TOKEN": TOKEN
}
req_graph = {
    "id": G_ID,
    "name": "ambition",
    "unit": "effort",
    "type": "int",
    "color": "ajisai",
}

# data = requests.post(url=f"{URL}/{USER}/graphs", json=req_graph, headers=head)
# print(data.text)

#3  PUSH PIXEL
today = dt.datetime.now()
today = today.strftime("%Y%m%d")
pixel_insert = {
    "date": today,
    "quantity": "10"
}
# data = requests.post(f"{URL}/{USER}/graphs/{G_ID}", json=pixel_insert, headers=head)
# print(data.text)

#4 update a pixel
pixel_update = {
    "quantity": "15"
}
data = requests.put(f"{URL}/{USER}/graphs/{G_ID}/{today}", json=pixel_update, headers=head)
print(data.text)

#5 DELETE PIXEL
# data = requests.delete(f"{URL}/{USER}/graphs/{G_ID}/{today}", headers=head)
# print(data.text)
