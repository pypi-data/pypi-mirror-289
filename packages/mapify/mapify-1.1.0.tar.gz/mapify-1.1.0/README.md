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
mapify.generate(map_name='map', map_type='json', seed=500)

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
Encrypted text: 94 142 161 82 200 16 82 198 46 45 182
Decrypted text: Hello world!
```

### Module: Generate
The **generate** module isn't necessary when using this package. It only exists to generate your own/new random map to, use based off an existing map.

This module only randomizes the already existing values. All parameters explained below:
```python
from mapify import generate

generate (
    map_name = "map-2",
    map_type = "json",
    seed = None,
    original_map = "map-1.toml",
    special_words = ["name", "I like python", "username", "password"]
)
```
- **Map name** - The name of the new generated map. If none given, then the program won't make a file.
- **Map type** - The type of file you prefer the map must be. Only **json or toml** is supported.
- **Seed** - The seed on which the map must be randomized. This can be used as actual key instead of a map file.
- **Original map** - The map where the new map must be based off. If none given, the standard **default.toml** will be used. This file is listed below.
- **Special words** - The words which need their own key in the new map. This way, is it easy to keep some words completely safe.

**Return value** - When executing this module, the **full** name of the new map format will be returned (E.g. "map.json"). You can catch it with a variable to use it when you're encrypting or decrypting.

### Module: Encrypt
The **encrypt** module is the main module when using this package. It transforms the input text into cipher text using the attached map.

All parameters explained below:
```python
from mapify import encrypt

encrypt (
    input_text = "I love Python!",
    used_map = None,
    strip_input=False
)
```
- **Input text** - The text which has to be encrypted.
- **Used map** - The map file which the program has to use to encrypt. If none given, the **default.toml** file will be used.
- **Strip input** - When reading different lines, there might be a \n on the end of an input string. When True, the program will filter it out.

**Return value** - When executing this module, the encrypted text in string format will be returned. You can catch it with a variable to use it in your own program.

### Module: Decrypt
The **decrypt** module is the second main module when using this package. It transforms cipher text back into readable text using the attached map.

All parameters explained below:
```python
from mapify import decrypt

decrypt (
    input_text = "51 34 29 17 24 23",
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

You don't have to stay at 1 character, like the **default.toml** file is build from. The program checks until it can find a reference. This means that you can even save this, which would encrypt "I love python" into "1 2"
```toml
[map]
    1 = "I lo"
    2 = "ve python"
```

You can already see why this can be safe. As long as the map file and/or seed when generating isn't exposed, is your text completely safe! Like your own password.

## Challenge
Still not convinced that it's safe? Try to crack this ciphertext!

main.py:
```python
# Imports
from mapify import encrypt, generate


# Setting variables
secrets = ["name"]
map_used = generate(map_name="map", special_words=secrets)

# Encrypting line per line
with open("famous-poem.txt") as poem:
    for line in poem:
        encrypted_line = encrypt(line, map_used)
        print(encrypted_line)
```
Example output:
```text
19 16 42 195 90 85 195 14 16 42 195 90 85 195 14 16 133 191 85 144 85 154 195 144 85 16 206 144 143 16 143 191 195 132 16 42 195 90 85 195 102
17 85 93 131 16 143 191 131 16 154 206 143 191 85 144 16 206 93 134 16 144 85 154 132 26 85 16 143 191 131 16 185 150
19 144 16 88 154 16 143 191 195 132 16 133 88 36 143 16 93 195 143 14 16 199 85 16 199 132 143 16 26 133 195 144 93 16 90 131 16 36 195 109 85
180 93 134 16 39 202 192 16 93 195 16 36 195 93 78 85 144 16 199 85 16 206 16 204 206 116 132 36 85 143 150
202 123 88 26 16 199 132 143 16 143 191 131 16 185 16 143 191 206 143 16 88 26 16 90 131 16 85 93 85 90 131 152
123 191 195 132 16 206 144 143 16 143 191 131 26 85 36 154 14 16 143 191 195 132 78 191 16 93 195 143 16 206 16 155 195 93 143 206 78 132 85 150
148 191 206 143 202 26 16 155 195 93 143 206 78 132 85 102 16 39 143 16 88 26 16 93 195 144 16 191 206 93 134 16 93 195 144 16 154 113 143
95 195 144 16 206 144 90 16 93 195 144 16 154 206 28 85 16 93 195 144 16 206 93 131 16 195 143 191 85 144 16 116 206 144 143
153 85 36 195 93 78 88 93 78 16 143 195 16 206 16 90 206 93 150 16 19 16 199 85 16 26 195 90 85 16 195 143 191 85 144 16 185 150
148 191 206 143 202 26 16 88 93 16 206 16 185 102 16 123 191 206 143 16 133 191 88 28 191 16 133 85 16 28 206 192 16 206 16 144 195 26 85
153 131 16 206 93 131 16 195 143 191 85 144 16 185 16 133 195 132 36 134 16 26 90 85 192 16 206 26 16 26 133 67 143 83
210 195 16 42 195 90 85 195 16 133 195 132 36 134 14 16 133 85 144 85 16 191 85 16 93 195 143 16 42 195 90 85 195 16 28 206 192 202 134 14
42 85 143 206 88 93 16 143 191 206 143 16 134 85 206 144 16 116 85 144 154 85 28 143 88 195 93 16 133 191 88 28 191 16 191 85 16 195 133 85 26
148 88 143 191 195 132 143 16 143 191 206 143 16 143 88 143 36 85 150 16 42 195 90 85 195 14 16 134 195 62 16 143 191 131 16 185 14
180 93 134 16 154 195 144 16 143 191 206 143 16 185 14 16 133 191 88 28 191 16 88 26 16 93 195 16 116 206 144 143 16 195 154 16 143 191 67 14
123 206 21 85 16 206 192 16 90 131 26 85 36 154 150
```