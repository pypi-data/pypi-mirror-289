from importlib import resources
import toml
import json
import random


def generate(original_map=None, return_type="toml", map_name=None, seed=None):
    # Sets seed if given for reusability
    if seed is not None:
        random.seed(seed)

    # Get the original map
    old_map = _load_map(original_map)

    # Extract the keys and values
    keys = list(old_map.keys())
    values = list(old_map.values())

    # Shuffle values
    random.shuffle(values)

    # Create a new map with shuffled values
    shuffled_map = {key: values[i] for i, key in enumerate(keys)}

    # Return the shuffled map in the desired return type
    if return_type == "json":
        new_map = {"map": shuffled_map}
        new_map_str = json.dumps(new_map, ensure_ascii=False, indent=4)
    else:
        new_map_str = "[map]\n"
        for key, value in shuffled_map.items():
            escaped_value = _escape_special_characters(value)
            new_map_str += f'\t{key} = "{escaped_value}"\n'

    if map_name is not None:
        with open(f"{map_name}.{return_type}", "w", encoding="UTF-8") as f:
            f.write(new_map_str)
            f.close()
    return new_map_str


def _escape_special_characters(value):
    escape_map = {
        '\n': '\\n',
        '\t': '\\t',
        '"': '\\',
        '\\': '\\\\'
    }
    for char, escape in escape_map.items():
        value = value.replace(char, escape)
    return value


def _load_map(original_map):
    directed_map = original_map if original_map else 'default.toml'
    if not (directed_map.endswith(".toml") or directed_map.endswith(".json")):
        raise ValueError("Invalid file type. Please provide a .toml or .json file.")

    try:
        if original_map:
            with open(directed_map) as f:
                if directed_map.endswith(".toml"):
                    data = toml.load(f)
                elif directed_map.endswith(".json"):
                    data = json.load(f)
        else:
            with resources.open_text('mapify', directed_map) as f:
                if directed_map.endswith(".toml"):
                    data = toml.load(f)
                elif directed_map.endswith(".json"):
                    data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{directed_map}' was not found.")
    except json.JSONDecodeError:
        raise ValueError(f"The file '{directed_map}' could not be parsed as JSON.")
    except toml.TomlDecodeError:
        raise ValueError(f"The file '{directed_map}' could not be parsed as TOML.")
    return data.get('map', {})