from .functions import load_map, default_map


def encrypt(input_text: str, used_map: str = None, strip_input=True):

    """
    Used to encrypt an input based off a given map.\n
    Returns the ciphertext (string).

    :param input_text: Required
    :param used_map:
    :param strip_input:
    """

    data = load_map(used_map, True)

    encoded_data = ""
    base = 0
    while base < len(input_text.strip() if strip_input else input_text):
        for i in range(len(input_text.strip() if strip_input else input_text), base, -1):
            custom_code = data.get(input_text.strip()[base:i] if strip_input else input_text[base:i], None)
            if custom_code is not None:
                encoded_data += custom_code + " "
                base = i
            else:
                default_code = default_map(input_text[base:i], True)
                if default_code is not None:
                    encoded_data += default_code + " "
                    base = i
    return encoded_data.strip()
