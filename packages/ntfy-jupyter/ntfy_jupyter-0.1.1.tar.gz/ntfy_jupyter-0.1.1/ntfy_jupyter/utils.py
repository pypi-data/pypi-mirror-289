import secrets
import string


def generate_key(length=16):
    """
    Generates a secure random key.

    Args:
        length (int): The length of the key to generate.

    Returns:
        str: The generated key.
    """
    characters = string.ascii_letters + string.digits
    key = ''.join(secrets.choice(characters) for _ in range(length))
    return key


def create_topic(base_name, key_length=22):
    """
    Creates a unique topic name by appending a cryptographic key.

    Args:
        base_name (str): The base name for the topic.
        key_length (int): The length of the cryptographic key.

    Returns:
        str: The unique topic name.
    """
    key = generate_key(length=key_length)
    return f"{base_name}-{key}"
