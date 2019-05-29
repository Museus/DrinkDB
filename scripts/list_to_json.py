import json

print("Run through list of ingredients, output to file")
input_file = raw_input("What is the file to read from?\n>")
output_file = raw_input("Enter the output file name.\n>")

ingredients_list = {
        'ingredients': []
        }

try:
    existing = open(output_file, 'r')
    ingredients_list['ingredients'] = json.load(existing)
    print("Found existing data, loaded.")
except IOError:
    print("No existing data found.")


with open(input_file, 'r') as input_list:
    for ingredient in input_list:
        print("Ingredient: " + ingredient)
        name = raw_input("name: ")
        ingredients_list['ingredients'].append({'name': name})

with open(output_file + '_new', 'w') as output:
    json.dump(ingredients_list, output)
