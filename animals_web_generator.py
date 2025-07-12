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
        if "name" in data:
            output+= f"Name: {data["name"]}\n"
        if "diet" in data["characteristics"]:
            output+=f"Diet: {data["characteristics"]["diet"]}\n"
        if "locations" in data:
            output+=f"Location: {data["locations"][0]}\n"
        if "type" in data["characteristics"]:
            output+=f"Type: {data["characteristics"]["type"]}\n"
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