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

animals_html_data = load_html_data('animals_template.html')

output = ''  # define an empty string
for animal in animals_data:
    # append information to each string
    if 'type' in animal['characteristics']:
        output += '<li class="cards__item">'
        output += f"Name:{animal['name']}<br/>\nDiet:{animal['characteristics']['diet']}<br/>\nLocation:{animal['locations'][0]}<br/>\nType:{animal['characteristics']['type']}<br/>\n\n"
        output += '</li>'
    else:
        output += '<li class="cards__item">'
        output += f"Name:{animal['name']}<br/>\nDiet:{animal['characteristics']['diet']}<br/>\nLocation:{animal['locations'][0]}<br/>\n\n"
        output += '</li>'
new_html_data = animals_html_data.replace('__REPLACE_ANIMALS_INFO__', output)
print(new_html_data)

save_to_html(new_html_data, 'animals_template.html')