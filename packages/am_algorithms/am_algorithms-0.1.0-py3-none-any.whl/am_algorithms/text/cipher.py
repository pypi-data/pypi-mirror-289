def caesar_cipher(text: str, key: float) -> str:
    """
    Encrypts the given text using the Caesar cipher.
    The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places
    down the alphabet.

    :param text: The text to be encrypted.
    :param key: The number of positions to shift each letter. Must be between 0 and 25.
    :return: The encrypted text.
    :raises ValueError: If the key is not within the range [0, 25].
    """
    if key < 0 or key > 25:
        raise ValueError("Key must be in the range between 0 and 25")

    n = 26
    ciphertext = []
    lower_shift = ord('a')
    upper_shift = ord('A')

    for c in text:
        if c.isalpha():
            offset = lower_shift if c.islower() else upper_shift
            ciphertext.append(chr(((ord(c) - offset + key) % n) + offset))
        else:
            ciphertext.append(c)

    return ''.join(ciphertext)


def transposition_cipher(text: str) -> str:
    """
    Encrypts the given text using a simple transposition cipher.
    In this cipher, pairs of characters in the text are swapped.

    :param text: The text to be encrypted. Its length must be even.
    :return: The encrypted text.
    :raises ValueError: If the length of the text is not even.
    """
    if len(text) % 2 != 0:
        raise ValueError("Text length must be even for transposition cipher")

    char_list = list(text)
    n = len(char_list)

    for i in range(0, n - 1, 2):
        char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]

    return ''.join(char_list)


def vigenere_cipher(text: str, key: str) -> str:
    """
    Encrypts the given text using the Vigenère cipher.
    The Vigenère cipher uses a keyword to shift each letter of the plaintext by a number of positions determined
    by the corresponding letter in the key.

    :param text: The text to be encrypted.
    :param key: The keyword used for encryption. It is converted to lowercase and repeated as necessary.
    :return: The encrypted text.
    """

    def _get_shift(char: str, key_char: str) -> str:
        base = ord('a') if char.islower() else ord('A')
        shift = ord(key_char) - ord('a')
        return chr((ord(char) - base + shift) % 26 + base)

    key = key.lower()
    ciphertext = []
    key_index = 0

    for c in text:
        ciphertext.append(_get_shift(c, key[key_index % len(key)]) if c.isalpha() else c)
        key_index += c.isalpha()

    return ''.join(ciphertext)