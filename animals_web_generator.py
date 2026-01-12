import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')
# print(animals_data)
print()
animals_list = []
for animal in animals_data:
    if 'type' in   animal['characteristics']:
        print(f"Name:{animal['name']}\nDiet:{animal['characteristics']['diet']}\nLocation:{animal['locations'][0]}\nType:{animal['characteristics']['type']}\n")
    else:
        print(
            f"Name:{animal['name']}\nDiet:{animal['characteristics']['diet']}\nLocation:{animal['locations'][0]}\n")

