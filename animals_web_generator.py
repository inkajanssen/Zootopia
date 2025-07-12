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


def get_skin_types(animals_data:list)->list:
    """
    Gather all skin types from json file
    :param animals_data:
    :return: a unique list of skin types
    """

    skin_types = []
    for data in animals_data:
        skin_types.append(data["characteristics"]["skin_type"])

    return list(set(skin_types))


def collect_animal_data(data:dict)->str:
    """
    Reads the content of  a single animals, collects its data
    :return: a string for an HTML card with the gathered information
    """

    output = ""
    output += '<li class="cards__item">'
    if "name" in data:
        output+= '<div class="card__title">' + f'{data["name"]}</div>\n'
    if "scientific_name" in data["taxonomy"]:
        output+= f'<dic class="card_subtitle"><i> {data["taxonomy"]["scientific_name"]}</i></div>\n'
    output += '<p class ="card__text">'
    output += '<ul>'
    if "diet" in data["characteristics"]:
        output+= '<li><strong>Diet:</strong>' + f' {data["characteristics"]["diet"]}</li>\n'
    if "locations" in data:
        output+= '<li><strong>Location:</strong>' + f' {data["locations"][0]}</li>\n'
    if "type" in data["characteristics"]:
        output+= '<li><strong>Type:</strong>' + f' {data["characteristics"]["type"]}</li>\n'
    output += '</ul>'
    output += '</p>'
    if "slogan" in data["characteristics"]:
        output += f'<div class="slogan"> <cite>{data["characteristics"]["slogan"]}</cite></div>\n'
    output += '</li>'
    return output


def main():
    """
    Read the content of the json file and the html template
    Gather all skin types and ask user which one they want
    Gather data about the animals with that skin type
    Create a new html file
    """

    animals_data = load_data('animals_data.json')
    html_content = load_html("animals_template.html")

    list_of_skin_types = get_skin_types(animals_data)
    while True:
        selected_skin_type = (
            input(f"Please select a skin type of the following ones"
                  f" {list_of_skin_types}:"))
        if selected_skin_type in list_of_skin_types:
            break
        else:
            print("Please enter a valid skin type!")


    output = ""
    for data in animals_data:
        if data["characteristics"]["skin_type"] == selected_skin_type:
            output += collect_animal_data(data)

    replace_info = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
    save_html("animals.html", replace_info)


if __name__ == '__main__':
    main()