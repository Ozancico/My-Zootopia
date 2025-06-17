import json


def read_json_file(file_path):
    """
    Reads and returns data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: The parsed JSON data.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def read_template_file(file_path):
    """
    Reads the HTML template file.

    Args:
        file_path (str): Path to the template file.

    Returns:
        str: The contents of the template file.
    """
    with open(file_path, 'r') as file:
        return file.read()


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

    # Location information
    if 'locations' in animal and len(animal['locations']) > 0:
        output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    # Type information (if available)
    if 'characteristics' in animal and 'type' in animal['characteristics']:
        output += f'      <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

    output += '    </p>\n'
    output += '  </li>\n'
    return output


def generate_animal_cards(animals):
    """
    Generates HTML for all animal cards.

    Args:
        animals (list): List of animal dictionaries.

    Returns:
        str: Combined HTML string of all animal cards.
    """
    return ''.join(serialize_animal(animal) for animal in animals)


def write_html_file(content, file_path):
    """
    Writes the final HTML content to a file.

    Args:
        content (str): The HTML content to write.
        file_path (str): Path to the output file.
    """
    with open(file_path, 'w') as file:
        file.write(content)


def replace_template(template, animals_html):
    """
    Replaces the placeholder in the template with generated content.

    Args:
        template (str): The HTML template string.
        animals_html (str): The generated HTML for all animals.

    Returns:
        str: The complete HTML with replaced content.
    """
    return template.replace('__REPLACE_ANIMALS_INFO__', animals_html)


def main():
    """
    Main function that orchestrates the HTML generation process.
    """
    # File paths
    json_file = 'animals_data.json'
    template_file = 'animals_template.html'
    output_file = 'animals.html'

    # Read input files
    animals_data = read_json_file(json_file)
    template_content = read_template_file(template_file)

    # Generate HTML content
    animals_html = generate_animal_cards(animals_data)
    final_html = replace_template(template_content, animals_html)

    # Write output file
    write_html_file(final_html, output_file)


if __name__ == '__main__':
    main()
