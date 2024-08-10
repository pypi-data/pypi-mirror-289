from importlib import resources
import toml
import json


def encode(input_text, used_map=None, multiple_lines=False):
    data = _load_mapping(used_map)

    encoded_data = ""
    words = input_text.strip().split()

    for i in range(len(words)):
        word_code = data.get(words[i], None)
        if word_code is not None:
            encoded_data += word_code + " "
        else:
            for char in words[i]:
                char_code = data.get(char, None)
                if char_code is not None:
                    encoded_data += char_code + " "
                else:
                    encoded_data += str(_default_map(char)) + " "

        if i != len(words) - 1:
            if multiple_lines:
                encoded_data += "\n"
            else:
                separator = data.get(" ", None)
                if separator is not None:
                    encoded_data += str(separator) + " "
                else:
                    encoded_data += _default_map(" ") + " "
    return encoded_data.strip()


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
    return {v: k for k, v in data.get('map', {}).items()}


def _default_map(value):
    with resources.open_text('mapify', 'default.toml') as f:
        data = toml.load(f)
        reversed_map = {v: k for k, v in data.get('map', {}).items()}
        char_code = reversed_map.get(value, None)
        return char_code if char_code is not None else "?"
