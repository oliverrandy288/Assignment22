import requests

# Task 1: Setting Up a Python Virtual Environment and Installing Packages
# Note: This part is just for reference. Ensure to set up your virtual environment as mentioned in the assignment.

# Task 2: Fetching Data from the Pokémon API
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    return data

def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data_list = [fetch_pokemon_data(name) for name in pokemon_names]

# Print Pokémon names and abilities
for pokemon in pokemon_data_list:
    name = pokemon['name']
    abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
    print(f"Pokémon: {name}")
    print("Abilities:", abilities)

# Calculate and print average weight
avg_weight = calculate_average_weight(pokemon_data_list)
print(f"Average Weight: {avg_weight} hectograms\n")

# Task 2: Fetch Data from a Space API
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    return [planet for planet in planets if planet['isPlanet']]

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda planet: planet['mass']['massValue'] if planet['mass'] else 0)
    return heaviest_planet['englishName'], heaviest_planet['mass']['massValue']

# Fetch and print planet data
planets = fetch_planet_data()
for planet in planets:
    name = planet['englishName']
    mass = planet['mass']['massValue'] if planet['mass'] else "Unknown"
    orbit_period = planet['sideralOrbit'] if planet['sideralOrbit'] else "Unknown"
    print(f"Planet: {name}, Mass: {mass} x 10^24 kg, Orbit Period: {orbit_period} days")

# Find and print the heaviest planet
name, mass = find_heaviest_planet(planets)
print(f"\nThe heaviest planet is {name} with a mass of {mass} x 10^24 kg.")