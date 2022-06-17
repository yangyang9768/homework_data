# Question 1
# In this session you used the Pokémon API to retrieve a single Pokémon.https://pokeapi.co/api/v2/pokemon/
# I want a program that can retrieve multiple Pokémon and save their names and moves to a file.
# Use a list to store about 6 Pokémon IDs. Then in a for loop call the API to retrieve the data for each Pokémon. Save their names and moves into a file called 'pokemon.txt'


import requests
request_url = 'https://pokeapi.co/api/v2/pokemon/'
pokemon = requests.get(request_url).json()['results']

with open('pokemon.txt', 'w') as text_file:
        for item in pokemon:
            text_file.write(item['name'] + '\n')
        
with open('pokemon.txt', 'r') as text_file:
    contents = text_file.read()
    print(contents)

# Question 2 (optional)

# Here is a link to a really cool API: https: // opentdb.com/
# Answer the following questions:
# ·        What is the name of this API?
# ·        What does it do?
# ·        Example URL to make a call to this API?
# ·        Example output?
