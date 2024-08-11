from importlib import resources
import toml
import json


def load_map(used_map, reverse=False):
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
    return {v: k for k, v in data.get('map', {}).items()} if reverse else data.get('map', {})


def default_map(value, reverse=False):
    with resources.open_text('mapify', 'default.toml') as f:
        data = toml.load(f)
        if reverse:
            reversed_map = {v: k for k, v in data.get('map', {}).items()}
        else:
            reversed_map = data.get('map', {})
        char_code = reversed_map.get(value, None)
        return char_code
