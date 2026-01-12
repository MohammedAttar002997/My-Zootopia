import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def load_html_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return handle.read()


def save_to_html(html_data,file_path):
    with open(file_path, "w") as handle:
        handle.write(html_data)

animals_data = load_data('animals_data.json')
# print(animals_data)
print()

# for animal in animals_data:
#     if 'type' in   animal['characteristics']:
#         print(f"Name:{animal['name']}\nDiet:{animal['characteristics']['diet']}\nLocation:{animal['locations'][0]}\nType:{animal['characteristics']['type']}\n")
#     else:
#         print(
#             f"Name:{animal['name']}\nDiet:{animal['characteristics']['diet']}\nLocation:{animal['locations'][0]}\n")

animals_html_data = load_html_data('animals_template.html')

output = ''  # define an empty string
for animal in animals_data:
    # append information to each string
    if 'type' in animal['characteristics']:
        output += f"Name:{animal['name']}\nDiet:{animal['characteristics']['diet']}\nLocation:{animal['locations'][0]}\nType:{animal['characteristics']['type']}\n\n"
    else:
        output += f"Name:{animal['name']}\nDiet:{animal['characteristics']['diet']}\nLocation:{animal['locations'][0]}\n\n"

new_html_data = animals_html_data.replace('__REPLACE_ANIMALS_INFO__', output)
save_to_html(new_html_data, 'animals_template.html')
print(new_html_data)