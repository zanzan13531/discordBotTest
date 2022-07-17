
import requests, json
from datetime import timezone 
import datetime 

#5f18848ead1d480065bcc03f

#servername = requests.get("https://api.minehut.com/server/punchpotat?byName=true").json()
"""
x = requests.post("https://api.minehut.com/users/login", {"email": "zanzan13531@gmail.com", "password": "Brianxu9!minehut"}).json()
while (x == None):
    print("a")
print(x)
data = requests.get("https://api.minehut.com/server/5f18848ead1d480065bcc03f/status", {'slgSessionId': 'c8c7b920-1e3d-4784-af8f-4dfb62f8a229', 'slgUserId': 'c440fad5-e173-4872-8167-a5ced4d13be6','_id': '5f18844ddc7b8900599c3f3d', 'token': 'e6782621-2794-451d-abb3-a4b39ed7b8ea', "email": "zanzan13531@gmail.com", "password": "Brianxu9!minehut"}).json()
print(data)
"""
data2 = requests.get("https://api.minehut.com/server/5f18848ead1d480065bcc03f").json()["server"]["last_online"]
print(data2)
  
# Getting the current date  
# and time 
dt = datetime.datetime.now() 
  
utc_time = dt.replace(tzinfo=timezone(datetime.timedelta(hours = -7))) 
utc_timestamp = utc_time.timestamp() 

utc_timestamp = utc_timestamp * 1000

print(utc_timestamp)

print(utc_timestamp - data2)
if ((utc_timestamp - data2) < 250000):
    print("online")