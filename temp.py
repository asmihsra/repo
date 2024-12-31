import requests

# Constants
ACCESS_TOKEN = "EAABwzLixnjYBO9P8kaT6GGK1LMuRCNZChXPLj4UrQMYnYinJGmsBKrsVqsRbEExfJP6APeeqYFTjAJAfwbhOWZC85rdbu5MuZCpvUijKftQyZCNsbdB9ihAiJMcveNfwVTKmjmCBHuGUghCwyWC1oeCg1YTjwLOBSXex6qzZAHYEARNKO5REZB53zWYfUtNWfOxgZDZD"
THREAD_ID = "61570647107451"  # Replace this with the actual thread/conversation ID
MESSAGE = "XYZ"

# API endpoint
url = f"https://graph.facebook.com/v15.0/t_{THREAD_ID}/"

# Headers
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

# Parameters
parameters = {
    'access_token': ACCESS_TOKEN,
    'message': MESSAGE
}

# Send the message
response = requests.post(url, data=parameters, headers=headers)

# Output the result
if response.status_code == 200:
    print(f"Message sent successfully: {MESSAGE}")
else:
    print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
