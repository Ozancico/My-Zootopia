import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_animal_output(data):
    output = ''
    for animal in data:
        output += '  <li class="cards__item">\n'
        if 'name' in animal:
            output += f'    <div class="card__title">{animal["name"]}</div>\n'
        output += '    <p class="card__text">\n'
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f'      <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
        if 'locations' in animal and animal['locations']:
            output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'
        if 'type' in animal:
            output += f'      <strong>Type:</strong> {animal["type"]}<br/>\n'
        output += '    </p>\n'
        output += '  </li>\n'
    return output

def replace_template(html_template_path, output_text, result_path):
    with open(html_template_path, "r") as template_file:
        template_content = template_file.read()

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output_text)

    with open(result_path, "w") as result_file:
        result_file.write(final_html)

    print(f"HTML successfully written to {result_path}")

# Programmstart
data = load_data('animals_data.json')
animal_info = generate_animal_output(data)
replace_template('animals_template.html', animal_info, 'animals.html')
