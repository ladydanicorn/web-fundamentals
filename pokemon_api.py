#Assignment 1

import requests

def fetch_pokemon_data(pokemon_name):
    """
    Fetch data for a specific Pokémon from the PokéAPI.
    
    Args:
        pokemon_name (str): Name of the Pokémon to fetch
        
    Returns:
        dict: JSON response containing Pokémon data
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data for {pokemon_name}: {e}")
        return None

def calculate_average_weight(pokemon_list):
    """
    Calculate the average weight of a list of Pokémon.
    
    Args:
        pokemon_list (list): List of Pokémon data dictionaries
        
    Returns:
        float: Average weight in kilograms
    """
    weights = [pokemon['weight']/10 for pokemon in pokemon_list if pokemon]  
    return sum(weights) / len(weights) if weights else 0

def display_pokemon_info(pokemon_data):
    """
    Display information about a Pokémon.
    
    Args:
        pokemon_data (dict): Pokémon data dictionary
    """
    if pokemon_data:
        print(f"\nPokémon: {pokemon_data['name'].capitalize()}")
        print("Abilities:")
        for ability in pokemon_data['abilities']:
            print(f"- {ability['ability']['name']}")
        print(f"Weight: {pokemon_data['weight']/10} kg")

def main():
    pokemon_names = ["pikachu", "bulbasaur", "charmander"]
    
    pokemon_data_list = []
    print("Fetching Pokémon data...")
    
    for name in pokemon_names:
        pokemon_data = fetch_pokemon_data(name)
        if pokemon_data:
            pokemon_data_list.append(pokemon_data)
            display_pokemon_info(pokemon_data)
    
    if pokemon_data_list:
        avg_weight = calculate_average_weight(pokemon_data_list)
        print(f"\nAverage weight of all Pokémon: {avg_weight:.2f} kg")

if __name__ == "__main__":
    main()
