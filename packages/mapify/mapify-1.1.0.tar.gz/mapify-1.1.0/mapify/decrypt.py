from .functions import load_map, default_map


def decrypt(input_text: str, used_map: str = None):

    """
    Used to decrypt ciphertext based off a map.\n
    Returns the decrypted data (string).

    :param input_text: Required
    :param used_map:
    """

    data = load_map(used_map)

    decoded_data = ""
    codes = input_text.strip().split()

    for code in codes:
        decoded_char = data.get(code, None)
        if decoded_char is not None:
            decoded_data += decoded_char
        else:
            decoded_default_char = default_map(code)
            if decoded_default_char is not None:
                decoded_data += decoded_default_char
    return decoded_data
