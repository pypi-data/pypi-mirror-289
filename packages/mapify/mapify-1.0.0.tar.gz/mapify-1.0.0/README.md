# 📂 Mapify
Encrypt and decrypt texts on a secure way using maps.

## Mapi*what*?
Mapify is a small **python package** made for easy encrypting texts. It can be used to save data on a secure way.

There are currently 3 functions available, which you can use:
- Encrypt
- Decrypt
- Generate

## How to get it?
By simply installing the package using ```pip install mapify``` are all files imported and ready to use.

## How to use it?
Like every python package is an easy `import` all you need. An example below:
```python
# Importing the package
import mapify


# Main code
text = "Hello world!"
print(f"Original text: {text}")

# Generate a random map, based off the standard default.toml file with seed 500 to reuse it later on. A "map.json" file will be generated.
mapify.generate(map_name='map', return_type='json', seed=500)

# We encrypt the text variable and use the newly generated map "map.json".
encrypted_text = mapify.encrypt(input_text=text, used_map="map.json")
print(f"Encrypted text: {encrypted_text}")

# We decrypt the encrypted text with the same map we used to encrypt it
decrypted_text = mapify.decrypt(input_text=encrypted_text, used_map="map.json")
print(f"Decrypted text: {decrypted_text}")
```
output:
```text
Original text: Hello world!
Encrypted text: 89 72 32 32 71 96 95 71 91 32 90 24
Decrypted text: Hello world!
```

### Module: Generate
The **generate** module isn't necessary when using this package. It only exists to generate your own/new random map to, use based off an existing map.

This module only randomizes the already existing values. All parameters explained below:
```python
from mapify import generate

generate (
    map_name = "map-2",
    return_type = "json",
    seed = None,
    original_map = "map-1.toml"
)
```
- **Map name** - The name of the new generated map. If none given, then the program won't make a file.
- **Return type** - The type of file you prefer the map must be. Only **json or toml** is supported.
- **Seed** - The seed on which the map must be randomized. This can be used as actual key instead of a map file.
- **Original map** - The map where the new map must be based off. If none given, the standard **default.toml** will be used. This file is listed below.

**Return value** - When executing this module, the json/toml format will be returned. You can catch it with a variable to print or use to copy in another file.

### Module: Encrypt
The **encrypt** module is the main module when using this package. It transforms the input text into cipher text using the attached map.

All parameters explained below:
```python
from mapify import encrypt

encrypt (
    input_text = "I love Python!",
    used_map = None,
    multiple_lines = True
)
```
- **Input text** - The text which has to be encrypted.
- **Used map** - The map file which the program has to use to encrypt. If none given, the **default.toml** file will be used.
- **Multiple lines** - The way the encrypted data has to be returned. True: Each word will be seperated per line. False: Cipher text seperated by whitespace.

**Return value** - When executing this module, the encrypted text in string format will be returned. You can catch it with a variable to use it in your own program.

### Module: Decrypt
The **decrypt** module is the second main module when using this package. It transforms cipher text back into readable text using the attached map.

All parameters explained below:
```python
from mapify import decrypt

decrypt (
    input_text = "1 30 4 70 109 203 4 8",
    used_map = None
)
```
- **Input text** - The text which has to be decrypted.
- **Used map** - The map file which the program has to use to decrypt. If none given, the **default.toml** file will be used.

**Return value** - When executing this module, the decrypted text in string format will be returned. You can catch it with a variable to use it in your own program.

## What are map files?
Map files are json/toml files which can be made or generated (copied + randomized) with the **generate** module. An example below:

```toml
[map]
    1 = "I"
    2 = "Love"
    3 = "Python"
```

The text "I love python" would become "1 2 3" in cipher text

You don't have to stay at 1 character, like the **default.toml** file is build from. The program checks word per word, then character per character. This means that **It's currently not possible to map multiple words in 1 value**.

You can already see why this can be safe. as long as the map file and/or seed when generating isn't exposed, is your text completely safe! Like your own password.

### Default.toml

Here is the entire default.toml file listed as reference to what all non-modified maps are based off:

```toml
["map"]
    # Numbers
    0 = "0"
    1 = "1"
    2 = "2"
    3 = "3"
    4 = "4"
    5 = "5"
    6 = "6"
    7 = "7"
    8 = "8"
    9 = "9"

    # Lowercase characters
    10 = "a"
    11 = "b"
    12 = "c"
    13 = "d"
    14 = "e"
    15 = "f"
    16 = "g"
    17 = "h"
    18 = "i"
    19 = "j"
    20 = "k"
    21 = "l"
    22 = "m"
    23 = "n"
    24 = "o"
    25 = "p"
    26 = "q"
    27 = "r"
    28 = "s"
    29 = "t"
    30 = "u"
    31 = "v"
    32 = "w"
    33 = "x"
    34 = "y"
    35 = "z"

    # Uppercase characters
    36 = "A"
    37 = "B"
    38 = "C"
    39 = "D"
    40 = "E"
    41 = "F"
    42 = "G"
    43 = "H"
    44 = "I"
    45 = "J"
    46 = "K"
    47 = "L"
    48 = "M"
    49 = "N"
    50 = "O"
    51 = "P"
    52 = "Q"
    53 = "R"
    54 = "S"
    55 = "T"
    56 = "U"
    57 = "V"
    58 = "W"
    59 = "X"
    60 = "Y"
    61 = "Z"

    # Symbols
    62 = "_"
    63 = "-"
    64 = "+"
    65 = "/"
    66 = "\\"
    67 = "|"
    68 = "*"
    69 = "="
    70 = "%"
    71 = "<"
    72 = ">"
    73 = "^"
    74 = ":"
    75 = ";"
    76 = "."
    77 = ","
    78 = "'"
    79 = "!"
    80 = "?"
    81 = "("
    82 = ")"
    83 = "["
    84 = "]"
    85 = "{"
    86 = "}"
    87 = "€"
    88 = "$"
    89 = "µ"
    90 = "£"
    91 = "`"
    92 = "´"
    93 = "@"
    94 = "#"
    95 = "&"
    96 = "~"
    97 = "\n"
    98 = "\t"
    99 = " "
```
This file will be improved later on for special characters.