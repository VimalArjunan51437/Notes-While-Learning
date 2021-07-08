# 1. Ask for user input -> character in pokemon
# 2. Create a dynamic url based on step 1
# 3. Fetch the data from the url in  step 2
# 4. Convert JSON to a dictionary
# 5. Print out pokemon data

import requests  #  Packages

pokemon_name = input("Enter the character name  :") # get input from user to fine the character

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"  # 

req = requests.get(url)

if req.status_code == 200: # to know about status of our url
    
    data = req.json() # storing JSON data to variable 

    print(f"Name of the pokemon is : {data['name']}")
    for ability in data['abilities']:
        print(ability['ability']['name'])
else:
    print(f"{req.status_code} code error")