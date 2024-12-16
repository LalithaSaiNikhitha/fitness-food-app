import json
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access your API credentials
API_KEY = os.getenv('API_KEY')
APP_ID = os.getenv('APP_ID')

def get_food_info(food_name):
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}
    data = {"query": food_name}
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def load_exercise_data(file_path):
    with open(file_path, 'r') as file:
        exercises = json.load(file)
    return exercises

def get_exercise_by_category(data, category):
    return [ex for ex in data if ex["category"].lower() == category.lower()]
