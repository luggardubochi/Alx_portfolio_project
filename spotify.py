#!/usr/bin/env python


import requests
import base64
import json

url = 'https://accounts.spotify.com/api/token'
headers = {}
data = {}

clientId = "8e6d84ed1ede44739df3bc59577cc19a"
clientSecret = "928ad332a24f4a758fc910157842bfcc"

message = f"{clientId}:{clientSecret}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')


headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"

r = requests.post(url, headers=headers, data=data)

token = r.json()['access_token']

# Step 2 - Use Access Token to call playlist endpoint

playlistId = "myPlaylistId"
playlistUrl = f"https://api.spotify.com/v1/playlists/{playlistId}"
headers = {
    "Authorization": "Bearer " + token
}

res = requests.get(url=playlistUrl, headers=headers)

print(json.dumps(res.json(), indent=2))
