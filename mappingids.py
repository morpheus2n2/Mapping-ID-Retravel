import requests
import yaml

# Prompt the user for the API key and file location
api_key = input("Enter your TMDb API key: ")
file_path = input("Enter the path to your YAML file: ")

# Load the YAML file
try:
    with open(file_path, 'r') as file:
        print(f"Opening file: {file_path}")
        data = yaml.safe_load(file)
        movies = data['metadata'].keys()
        print(f"Loaded movies: {movies}")
except FileNotFoundError:
    print(f"YAML file not found at path: {file_path}")
    exit()
except yaml.YAMLError as exc:
    print(f"Error in YAML file: {exc}")
    exit()

# Base URL for TMDb search
base_url = 'https://api.themoviedb.org/3/search/movie'

# Function to get movie ID
def get_movie_id(movie_name):
    params = {
        'api_key': api_key,
        'query': movie_name
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        if data['results']:
            return data['results'][0]['id']
        else:
            print(f"No results found for {movie_name}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    return None

# Function to clean movie title
def clean_movie_title(movie_name):
    # Remove year from the title
    if '(' in movie_name:
        movie_name = movie_name.split('(')[0].strip()
    return movie_name

# Retrieve IDs for each movie and update the YAML data
existing_ids = set()
for movie in movies:
    cleaned_movie = clean_movie_title(movie)
    print(f"Searching for: {cleaned_movie}")  # Debugging line
    movie_id = get_movie_id(cleaned_movie)
    if movie_id:
        if movie_id in existing_ids:
            confirm = input(f"Duplicate ID {movie_id} found for {movie}. Do you want to proceed? (yes/no): ")
            if confirm.lower() != 'yes':
                print(f"Skipping {movie} due to duplicate ID.")
                continue
        data['metadata'][movie]['mapping_ID'] = movie_id
        existing_ids.add(movie_id)
        print(f"Found ID for {movie}: {movie_id}")  # Debugging line
    else:
        print(f"Failed to retrieve ID for {movie}")

# Save the updated data back to the YAML file without modifying url_poster
with open(file_path, 'w') as file:
    yaml.safe_dump(data, file, default_flow_style=False)

print("Updated YAML file with TMDb IDs in mapping_ID fields.")
