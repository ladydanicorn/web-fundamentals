# Assignment 2

import requests
from typing import List, Tuple, Dict
import json
from operator import itemgetter

def fetch_planet_data() -> List[Dict]:
    """
    Fetches planet data from the Solar System OpenData API.
    Returns a list of planet dictionaries with formatted data.
    """
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()['bodies']
        
        planets = []
        for body in data:
            if body.get('isPlanet', False):
                planet_info = {
                    'name': body['englishName'],
                    'mass': body['mass']['massValue'] * (10 ** body['mass']['massExponent']),
                    'orbit_period': body['sideralOrbit'],
                    'gravity': body['gravity'],
                    'escape_velocity': body['escape']  # in km/s
                }
                planets.append(planet_info)
        
        return sorted(planets, key=lambda x: x['name'])
    
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def display_planet_info(planets: List[Dict]) -> None:
    """
    Displays formatted information about each planet.
    """
    print("\nPlanet Information:")
    print("-" * 80)
    print(f"{'Planet':<10} {'Mass (kg)':<20} {'Orbit Period (days)':<20} {'Gravity (m/s²)':<15}")
    print("-" * 80)
    
    for planet in planets:
        print(f"{planet['name']:<10} {planet['mass']:.2e} {planet['orbit_period']:<20.2f} {planet['gravity']:<15.2f}")

def find_heaviest_planet(planets: List[Dict]) -> Tuple[str, float]:
    """
    Finds the planet with the highest mass.
    Returns a tuple of (planet_name, mass).
    """
    if not planets:
        return ("No data available", 0)
    
    heaviest = max(planets, key=lambda x: x['mass'])
    return (heaviest['name'], heaviest['mass'])

def analyze_planets(planets: List[Dict]) -> None:
    """
    Performs various analyses on the planet data.
    """
    if not planets:
        print("No planet data available for analysis.")
        return

    longest_orbit = max(planets, key=lambda x: x['orbit_period'])
    
    highest_escape = max(planets, key=lambda x: x['escape_velocity'])
    
    print("\nPlanetary Analysis:")
    print("-" * 40)
    
    heaviest_name, heaviest_mass = find_heaviest_planet(planets)
    print(f"Heaviest Planet: {heaviest_name} ({heaviest_mass:.2e} kg)")
    
    print(f"Longest Orbit: {longest_orbit['name']} ({longest_orbit['orbit_period']:.2f} days)")
    
    print(f"Highest Escape Velocity: {highest_escape['name']} ({highest_escape['escape_velocity']:.2f} km/s)")

def main():
    print("Fetching planet data...")
    planets = fetch_planet_data()
    
    if planets:
        display_planet_info(planets)
        
        analyze_planets(planets)
    else:
        print("Failed to fetch planet data. Please check your internet connection and try again.")

if __name__ == "__main__":
    main()