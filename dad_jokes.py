import requests
from pyfiglet import figlet_format
from random import choice

# text display for the application
header = figlet_format("DAD'S GOT JOKES")

print(header)

# URL for the jokes
url = "https://icanhazdadjoke.com/search"

# input for requested joke
user_input = input("What would you like to hear a joke about? ")

# code for generating a http request and handling the response
resoponse = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input, "limit": 1}
).json()

# pulling jokes from JSON
user_joke = response["results"]

# code used for taking the total jokes and displaying one of them
num_jokes = response["total_jokes"]
if num_jokes > 1:
    print(f"I have {num_jokes} jokes about {user_input}, here is one:")
    print(choice(user_joke)['joke'])
elif num_jokes == 1:
    print(f"I only have one joke about {user_input}, here it is:")
    print(user_joke[0]['joke'])
else:
    print(f"Sorry, I don't have any jokes about {user_input}")