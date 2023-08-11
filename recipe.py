# Import requests, BeautifulSoup and json modules
import requests
from bs4 import BeautifulSoup
import json

# Define the URL of the website
url = "https://whatsfordinner.net/Whats-for-dinner-recipes-Refresh.html?#recipe"

# Get the HTML content of the website
response = requests.get(url)
html = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the div element that contains the recipe information
recipe_div = soup.find("div", id="recipe")

# Get the name of the dish from the h2 element
name = recipe_div.find("h2").text

# Get the description of the dish from the p element
description = recipe_div.find("p").text

# Get the image URL of the dish from the img element
image_url = recipe_div.find("img")["src"]

# Download the image and save it in a directory called "images"
image_response = requests.get(image_url)
image_name = image_url.split("/")[-1]
image_path = "images/" + image_name
with open(image_path, "wb") as f:
    f.write(image_response.content)

# Get the ingredients of the dish from the ul element
ingredients = []
ul = recipe_div.find("ul")
for li in ul.find_all("li"):
    ingredients.append(li.text)

# Get the steps of the dish from the ol element
steps = []
ol = recipe_div.find("ol")
for li in ol.find_all("li"):
    steps.append(li.text)

# Create a JSON list with the name, description, ingredients, steps and image path of the dish
recipe_list = [{"name": name, "description": description, "ingredients": ingredients, "steps": steps, "image_path": image_path}]

# Print the JSON list in a formatted way
print(json.dumps(recipe_list, indent=4))
