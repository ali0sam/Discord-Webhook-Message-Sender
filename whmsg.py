from discord_webhook import DiscordWebhook
from time import sleep
import os
import json

with open("data.json") as f:
	data = json.load(f)
	weburl = data["webhook"]
	user = data["name"]
	icon = data["icon"]

def response():
	response = webhook.execute()

count = 0
while count <= 50:
	os.system("cls")
	os.system(f"title Messages sent: {count}")
	msg = input("Message: ")
	webhook = DiscordWebhook(url=weburl, content=msg, username=user, avatar_url=icon)
	response()
	count += 1

