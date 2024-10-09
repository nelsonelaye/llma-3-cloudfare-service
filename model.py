import requests
import requests
from dotenv import load_dotenv
import os

load_dotenv()


model = "@cf/meta/llama-3-8b-instruct"
API_BASE_URL =os.getenv('API_BASE_URL')
API_KEY = os.getenv("API_TOKEN")

headers = {"Authorization": f"Bearer {API_KEY}"}

def run( query):
    input = { "messages":  [
    { "role": "user", "content": query}
] }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()



inputs = [
    { "role": "system", "content": "You are a friendly assistan that helps write stories" },
    { "role": "user", "content": "Write a short story about a llama that goes on a journey to find an orange cloud "}
]
# output = run("Hi")
# print(output)