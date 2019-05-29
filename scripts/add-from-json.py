from pymongo import MongoClient
import json

print("This script is used to load a list of recipes into the database.")
print("This will remove all previous recipes, so only use it to initialize the list.")
filename = raw_input("Input the path to the file you'd like to import.\n>")

#uri = "mongodb+srv://Museus:<password>@jredding-recipebook-3cs5y.mongodb.net/test?retryWrites=true"
client = MongoClient()

resources = client['RecipeBook'].resources

with open(filename, 'r') as input_file:
    ingredient_list = json.load(input_file)

resources.insert_one(ingredient_list)
