from data_fetcher import fetch_data



def load_html_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return handle.read()


def save_to_html(html_data,file_path):
    with open(file_path, "w") as handle:
        handle.write(html_data)


def serialize_animal(animal_obj):
    output_obj = ''  # define an empty string

    output_obj += '<li class="cards__item">'
    output_obj += f'<div class="card__title">{animal_obj['name']}</div>'
    output_obj += '<p class="card__text">'
    output_obj += '<ul class="animal__items">'
    output_obj += f'<li class="diet_type"><strong>Diet:  </strong>{animal_obj['characteristics']['diet']}</li>\n'
    output_obj += f'<li class="animal__country"><strong>Location:  </strong>{animal_obj['locations'][0]}</li>\n'

    # append information to each string
    if 'type' in animal_obj['characteristics']:
        output_obj += f'<li class="fox__type"><strong>Type:  </strong>{animal_obj['characteristics']['type']} </li>\n'
    if 'group' in animal_obj['characteristics']:
        output_obj += f'<li class="fox__group"><strong>Group:  </strong>{animal_obj['characteristics']['group']}</li>\n'
    output_obj += '</ul>'
    output_obj += '</p>'
    output_obj += '</li>'
    return output_obj



def main():
    fetch_data("Fox")
    animals_data = fetch_data("Fox")
    # animals_html_data = load_html_data('animals_template.html')
    #
    # output = ''  # define an empty string
    # for animal in animals_data:
    #     output += serialize_animal(animal)
    #
    # new_html_data = animals_html_data.replace('__REPLACE_ANIMALS_INFO__', output)
    # save_to_html(new_html_data, 'animals.html')



if __name__ == '__main__':
    main()