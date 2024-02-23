from webserver import keep_alive
import requests

channelID = 1210206247488454716
headers = {
    "authorization":
    "MTE3ODUxNjkxMDQwOTc5MzU5OA.G4edU9.mYBH6yNqF3f6Qn9hReGYuY2TDhC-uH3CvoTBsg"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
