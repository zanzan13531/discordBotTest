import discord
import asyncio
import requests, json

from datetime import timezone 
import datetime 
#print(discord.__version__)  # check to make sure at least once you're on the right version!

token = "NzM1NjgyNTYxNTI2ODU3NzY4.Xxj0nQ.FdunyoUP5XquTVbv-II62lNgC5Q"

client = discord.Client()  # starts the discord client.


@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.
    client.loop.create_task(status_task())

async def status_task():
    while True:
        dt = datetime.datetime.now() 
        utc_time = dt.replace(tzinfo=timezone(datetime.timedelta(hours = -7))) 
        utc_timestamp = utc_time.timestamp() 
        utc_timestamp = utc_timestamp * 1000

        data2 = requests.get("https://api.minehut.com/server/5f18848ead1d480065bcc03f").json()["server"]["last_online"]

        if ((utc_timestamp - data2) < 250000):
            await client.change_presence(activity = discord.Game(name="online"))
        else:
            await client.change_presence(activity = discord.Game(name="offline"))

        await asyncio.sleep(60)

client.run(token)  # recall my token was saved!