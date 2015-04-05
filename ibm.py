import requests
import json

url="https://gateway.watsonplatform.net/personality-insights/api"
username="80662f4f-763a-488a-9735-6a82f906fe6f"
password="Ren5g0rlLWEv"
input_data = {
    #'sid' : 'ie-en-news',
    'txt' : "The IBM Watson™ Personality Insights service provides an Application Programming Interface (API) that enables applications to derive insights from social media, enterprise data, or other digital communications. The service uses linguistic analytics to infer personality and social characteristics, including Big Five, Needs, and Values, from text. These insights help businesses to understand their clients' preferences and improve customer satisfaction by anticipating customer needs and recommending future actions. This allows businesses to improve client acquisition, retention, and engagement, and to strengthen relations with their clients.The IBM Watson™ Personality Insights service provides an Application Programming Interface (API) that enables applications to derive insights from social media, enterprise data, or other digital communications. The service uses linguistic analytics to infer personality and social characteristics, including Big Five, Needs, and Values, from text. These insights help businesses to understand their clients' preferences and improve customer satisfaction by anticipating customer needs and recommending future actions. This allows businesses to improve client acquisition, retention, and engagement, and to strengthen relations with their clients."
}

response = requests.post(url, auth=(username, password), data=input_data)
try:
    response.raise_for_status()
    print response.text
except requests.exceptions.HTTPError as e:
    print("And you get an HTTPError: %s"% e.message)
