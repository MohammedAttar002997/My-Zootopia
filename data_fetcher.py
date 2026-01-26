import requests
import os
from dotenv import load_dotenv

load_dotenv()

ANIMALS_API_KEY = os.getenv('API_KEY')
ANIMALS_URL = f"https://api.api-ninjas.com/v1/animals?X-Api-Key={ANIMALS_API_KEY}&name="


def fetch_data(name):
    final_url = ANIMALS_URL + name
    response = requests.get(final_url)
    res = response.json()
    return res