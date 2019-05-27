from pymongo import MongoClient
import json

uri = "mongodb+srv://AtlasRO:@jredding-recipebook-3cs5y.mongodb.net/test?retryWrites=true"
client = MongoClient(uri)

recipes = client['RecipeBook'].recipes

print(recipes.insert_one(drink);


