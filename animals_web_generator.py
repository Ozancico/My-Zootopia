import json


def load_data(file_path):
    """
    Loads a JSON file and returns its content as a Python object.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list[dict]: A list of animal data dictionaries.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """
    Converts a single animal dictionary into a formatted HTML <li> card.

    Args:
        animal (dict): A dictionary containing animal data.

    Returns:
        str: An HTML string representing the animal card.
    """
    output = '  <li class="cards__item">\n'

    # Animal name as the card title
    if 'name' in animal:
        output += f'    <div class="card__title">{animal["name"]}</div>\n'

    # Begin card description
    output += '    <p class="card__text">\n'

    # Diet information
    if "characteristics" in animal and 'diet' in animal['characteristics']:
        output += f'      <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

    # First listed location (if available)
    if "locations" in animal and animal['locations']:
        output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    # Animal type (e.g., mammal, bird, etc.)
    if "characteristics" in animal and 'type' in animal['characteristics']:
        output += f'      <strong>Type:</strong> {animal['characteristics']["type"]}<br/>\n'

    # End description and list item
    output += '    </p>\n'
    output += '  </li>\n'
    return output


def generate_animal_output(data):
    """
    Generates the full HTML block with cards for all animals in the dataset.

    Args:
        data (list[dict]): A list of animal dictionaries.

    Returns:
        str: A concatenated HTML string with all animal cards.
    """
    return ''.join(serialize_animal(animal) for animal in data)


def replace_template(html_template_path, output_text, result_path):
    """
    Replaces a placeholder in the HTML template with generated animal HTML,
    and writes the result to a new file.

    Args:
        html_template_path (str): Path to the template HTML file.
        output_text (str): Generated HTML for animals.
        result_path (str): Output path for the final HTML file.
    """
    with open(html_template_path, "r") as template_file:
        template_content = template_file.read()

    # Replace the placeholder with generated content
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output_text)

    # Write final HTML to file
    with open(result_path, "w") as result_file:
        result_file.write(final_html)

    print(f"✅ HTML successfully written to {result_path}")


# Entry point of the script
if __name__ == "__main__":
    # Load animal data from JSON file
    data = load_data("animals_data.json")

    # Generate animal cards as HTML
    animal_info = generate_animal_output(data)

    # Inject the generated HTML into the template and save the result
    replace_template("animals_template.html", animal_info, "animals.html")
