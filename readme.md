```markdown
# TMDb Mapping ID Updater

This script updates the `mapping_ID` fields in a YAML file with movie IDs retrieved from The Movie Database (TMDb) API.

## Prerequisites

- Python 3.x
- `requests` library
- `PyYAML` library

You can install the required libraries using pip:

```sh
pip install requests pyyaml
```

## Usage

1. Ensure you have a TMDb API key. You can get one by creating an account on [TMDb](https://www.themoviedb.org/) and generating an API key from your account settings.

2. Prepare your YAML file with the following structure:

```yaml
metadata:
  Movie Title (Year):
    mapping_ID:
    url_poster: <URL or leave empty>
```

Example:

```yaml
metadata:
  101 Dalmatians (1961):
    mapping_ID:
    url_poster: https://example.com/poster.jpg
  Aladdin (1992):
    mapping_ID:
    url_poster:
```

3. Run the script:

```sh
python mappingids.py
```

4. Enter your TMDb API key and the path to your YAML file when prompted.

## How It Works

1. The script prompts the user for a TMDb API key and the path to the YAML file.
2. It loads the YAML file and extracts the movie titles.
3. For each movie title, it removes the year from the title for a cleaner search query.
4. It sends a request to the TMDb API to search for the movie and retrieves the movie ID.
5. If a duplicate movie ID is found, the script prompts the user for confirmation before proceeding.
6. The script updates the `mapping_ID` field in the YAML file with the retrieved movie ID.
7. The updated YAML file is saved back to the specified path without modifying the `url_poster` fields.

## Notes

- The script does not modify the `url_poster` fields in the YAML file.
- If no results are found for a movie, the `mapping_ID` field remains empty.
- The script handles duplicate movie IDs by prompting the user for confirmation.

## Example Output

```sh
Enter your TMDb API key: your_api_key
Enter the path to your YAML file: /path/to/your/file.yml
Opening file: /path/to/your/file.yml
Loaded movies: dict_keys(['101 Dalmatians (1961)', 'Aladdin (1992)', ...])
Searching for: 101 Dalmatians
Found ID for 101 Dalmatians (1961): 11674
Searching for: Aladdin
Found ID for Aladdin (1992): 812
...
Updated YAML file with TMDb IDs in mapping_ID fields.
```

## License

This project is licensed under the MIT License.
```
