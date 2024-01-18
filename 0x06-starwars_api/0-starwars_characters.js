#!/usr/bin/node
"""
Write a script that prints all
characters of a Star Wars movies
"""
import requests
import sys

def get_characters(movie_id):
    "SWAPI base URL"
    base_url = "https://swapi-api.alx-tools.com/api/"

    "Endpoint for films"
    films_endpoint = f"{base_url}films/{movie_id}/"

    try:
        "Get information about the movie"
        response = requests.get(films_endpoint)
        response.raise_for_status()
        movie_data = response.json()

        "Extract character URLs from the movie data"
        character_urls = movie_data["characters"]

        "Fetch character names using the character URLs"
        for character_url in character_urls:
            character_response = requests.get(character_url)
            character_response.raise_for_status()
            character_data = character_response.json()
            print(character_data["name"])

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <Movie_ID>")
        sys.exit(1)

    movie_id = sys.argv[1]

    try:
        movie_id = int(movie_id)
    except ValueError:
        print("Error: Movie ID must be an integer.")
        sys.exit(1)

    get_characters(movie_id)

