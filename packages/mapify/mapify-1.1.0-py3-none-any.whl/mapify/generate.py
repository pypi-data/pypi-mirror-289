from .functions import load_map
from typing import Union
import random
import json


def generate(map_name: str, original_map: str = None, map_type: str = "toml", seed: Union[str, int, None] = None, special_words: list = []):

    """
    Used to generate a new map based off another map.\n
    Returns the full name of the generated map (string).

    :param map_name: Required
    :param original_map:
    :param map_type:
    :param seed:
    :param special_words:
    """

    # Sets seed if given for reusability
    if seed is not None:
        random.seed(seed)

    # Get the original map
    old_map = load_map(original_map)

    # Determine the next available starting index for special words
    if isinstance(old_map, dict):
        keys = list(old_map.keys())
        numeric_keys = [int(key) for key in keys if key.isdigit()]
        next_index = max(numeric_keys, default=-1) + 1
    else:
        next_index = 0

    # Create a new map including special words
    updated_map = old_map.copy()  # Copy original map
    for i, word in enumerate(special_words):
        updated_map[next_index + i] = word

    # Remove entries where values contain special characters
    filtered_map = {key: value for key, value in updated_map.items() if _contains_special_characters(value)}

    # Extract the keys and values
    keys = list(filtered_map.keys())
    values = list(filtered_map.values())

    # Shuffle values
    random.shuffle(values)

    # Create a new map with shuffled values
    shuffled_map = {key: values[i] for i, key in enumerate(keys)}

    # Return the shuffled map in the desired return type
    if map_type == "json":
        new_map = {"map": shuffled_map}
        new_map_str = json.dumps(new_map, ensure_ascii=False, indent=4)
    else:
        new_map_str = "[map]\n"
        for key, value in shuffled_map.items():
            escaped_value = _escape_special_characters(value)
            new_map_str += f'\t{key} = "{escaped_value}"\n'

    file_name = f"{map_name}.{map_type}"
    with open(file_name, "w", encoding="UTF-8") as f:
        f.write(new_map_str)
    return file_name


def _contains_special_characters(value):
    # Check if value contains special characters to be excluded
    special_chars = {'\n', '\t', '"', '\\'}
    return not any(char in value for char in special_chars)


def _escape_special_characters(value):
    # Simply return the value without escaping
    return value
