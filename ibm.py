import requests
import json

url="https://gateway.watsonplatform.net/personality-insights/api"
username="80662f4f-763a-488a-9735-6a82f906fe6f"
password="Ren5g0rlLWEv"
input_data = {
    #'sid' : 'ie-en-news',
    'txt' : "Call me Ishmael. Some years ago-never mind how long precisely-having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people's hats off-then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me."
}

response = requests.post(url, auth=(username, password), data=input_data)
try:
    response.raise_for_status()
    print response.text
except requests.exceptions.HTTPError as e:
    print("And you get an HTTPError: %s"% e.message)