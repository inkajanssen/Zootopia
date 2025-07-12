import json

def load_data(file_path):
  """ Loads a JSON file"""

  with open(file_path, "r") as handle:
    return json.load(handle)


def print_animal_data(data:dict):
    """
    Reads the content of animals_data.json, iterates through the animals,
    print data
    :return: Name, Diet, The first location from the locations list,Type
    """

    if "name" in data:
        print(f"Name: {data["name"]}")
    if "diet" in data["characteristics"]:
        print(f"Diet: {data["characteristics"]["diet"]}")
    if "locations" in data:
        print(f"Location: {data["locations"][0]}")
    if "type" in data["characteristics"]:
        print(f"Type: {data["characteristics"]["type"]}")
    print("---")


def main():
    """
    Read the content of the file
    """
    animals_data = load_data('animals_data.json')
    for data in animals_data:
        print_animal_data(data)


if __name__ == '__main__':
    main()