import json

def load_data(file_path):
  """ Loads a JSON file"""

  with open(file_path, "r", encoding='utf-8') as handle:
    return json.load(handle)


def load_html(file_path):
    """Load the content of an HTML file"""

    with open(file_path, "r", encoding='utf-8') as handle:
        return handle.read()


def save_html(file_path, content):
    """Save the content to an HTML file"""

    with open(file_path, "w", encoding='utf-8') as handle:
        return handle.write(content)


def collect_animal_data(animal_data:list):
    """
    Reads the content of animals_data.json, iterates through the animals,
    print data
    :return: Name, Diet, The first location from the locations list,Type
    """

    output = ""
    for data in animal_data:
        output += '<li class="cards__item">'
        if "name" in data:
            output+= '<div class="card__title">' + f'{data["name"]}</div>\n'
        output += '<p class ="card__text">'
        if "diet" in data["characteristics"]:
            output+= '<strong>Diet:</strong>' + f' {data["characteristics"]["diet"]}<br/>\n'
        if "locations" in data:
            output+= '<strong>Location:</strong>' + f' {data["locations"][0]}<br/>\n'
        if "type" in data["characteristics"]:
            output+= '<strong>Type:</strong>' + f' {data["characteristics"]["type"]}<br/>\n'
        output += '</p>'
        output += '</li>'
    return output


def main():
    """
    Read the content of the json file and the html template
    Gather some data about the animals
    Create a new html file
    """
    animals_data = load_data('animals_data.json')
    html_content = load_html("animals_template.html")
    output = collect_animal_data(animals_data)
    replace_info = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
    save_html("animals.html", replace_info)


if __name__ == '__main__':
    main()