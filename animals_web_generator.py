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


def collect_animal_data(data:dict):
    """
    Reads the content of  a single animals, collects its data
    :return: an HTML card with the gathered information
    """

    output = ""
    output += '<li class="cards__item">'
    if "name" in data:
        output+= '<div class="card__title">' + f'{data["name"]}</div>\n'
    if "scientific_name" in data["taxonomy"]:
        output+= f'<small><i> {data["taxonomy"]["scientific_name"]}</i></small><br/>\n'
    output += '<p class ="card__text">'
    if "diet" in data["characteristics"]:
        output+= '<strong>Diet:</strong>' + f' {data["characteristics"]["diet"]}<br/>\n'
    if "locations" in data:
        output+= '<strong>Location:</strong>' + f' {data["locations"][0]}<br/>\n'
    if "type" in data["characteristics"]:
        output+= '<strong>Type:</strong>' + f' {data["characteristics"]["type"]}<br/>\n'
    if "slogan" in data["characteristics"]:
        output += '<br>'
        output += f'<cite>{data["characteristics"]["slogan"]}</cite><br/>\n'
    output += '</p>'
    output += '</li>'
    return output


def main():
    """
    Read the content of the json file and the html template
    Gather data about the animals
    Create a new html file
    """

    animals_data = load_data('animals_data.json')
    html_content = load_html("animals_template.html")

    output = ""
    for data in animals_data:
        output += collect_animal_data(data)

    replace_info = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
    save_html("animals.html", replace_info)


if __name__ == '__main__':
    main()