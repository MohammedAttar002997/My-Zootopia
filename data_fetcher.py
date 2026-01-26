import requests


ANIMALS_API_KEY = "eNWURD45UUuOWclOytSGcJTM5NzSaakXDl6r3Ztm"
ANIMALS_URL = f"https://api.api-ninjas.com/v1/animals?X-Api-Key={ANIMALS_API_KEY}&name="


def fetch_data(name):
    final_url = ANIMALS_URL + name
    response = requests.get(final_url)
    res = response.json()
    return res