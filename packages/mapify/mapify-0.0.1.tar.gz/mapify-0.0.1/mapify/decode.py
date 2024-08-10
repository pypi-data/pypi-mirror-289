from importlib import resources
import toml
import json


def decode(encoded_text, used_map=None):
    data = _load_mapping(used_map)

    decoded_data = ""
    codes = encoded_text.strip().split()

    for code in codes:
        decoded_char = data.get(code, None)
        if decoded_char is not None:
            decoded_data += decoded_char
        else:
            decoded_data += _default_map(code)
    return decoded_data


def _load_mapping(used_map):
    directed_map = used_map if used_map else 'default.toml'
    if not (directed_map.endswith(".toml") or directed_map.endswith(".json")):
        raise ValueError("Invalid file type. Please provide a .toml or .json file.")

    try:
        if used_map:
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


def _default_map(value):
    with resources.open_text('mapify', 'default.toml') as f:
        data = toml.load(f)
        reversed_map = data.get('map', {})
        char_code = reversed_map.get(value, None)
        return char_code if char_code is not None else "?"
