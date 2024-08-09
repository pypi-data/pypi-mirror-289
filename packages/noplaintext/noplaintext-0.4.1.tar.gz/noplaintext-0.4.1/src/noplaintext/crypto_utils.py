from cryptography.fernet import Fernet
import os
import logging

LOGGER = logging.getLogger(__name__)

def generate_key(file_path):
    """
    Generate a new encryption key and save it to the specified file.

    Args:
        file_path (str): The path to the file where the generated key will be saved.

    Raises:
        Exception: If there is an error while generating or saving the key.
    """
    try:
        key = Fernet.generate_key()
        with open(file_path, "wb") as key_file:
            key_file.write(key)
    except Exception:
        LOGGER.exception(f"An error occurred while generating key file '{file_path}'.")
        raise
    LOGGER.debug(f"Generated key file '{file_path}'.")


def load_key(file_path: str):
    """
    Load an encryption key from the specified file.

    Args:
        file_path (str): The path to the file from which the key will be loaded.

    Returns:
        bytes: The encryption key read from the file.

    Raises:
        Exception: If there is an error while loading the key.
    """
    try:
        with open(file_path, "rb") as key_file:
            key = key_file.read()
    except Exception:
        LOGGER.exception(f"An error occurred while loading key file '{file_path}'.")
        raise
    LOGGER.debug(f"Loaded key file '{file_path}'.")
    return key
    

def encrypt(message, key_file_path):
    """
    Encrypt a message using the key from the specified file.

    Args:
        message (str): The message to be encrypted.
        key_file_path (str): The path to the file containing the encryption key.

    Returns:
        bytes: The encrypted message.

    Raises:
        Exception: If there is an error while encrypting the message.
    """
    try:
        cipher_suite = Fernet(load_key(key_file_path))
        encrypted_message = cipher_suite.encrypt(message.encode())
    except Exception:
        LOGGER.exception('An error occurred while encrypting the message.')
        raise
    LOGGER.debug('Encrypted message successfully.')
    return encrypted_message

def decrypt(encrypted_message, key_file_path):
    """
    Decrypt an encrypted message using the key from the specified file.

    Args:
        encrypted_message (bytes): The message to be decrypted.
        key_file_path (str): The path to the file containing the decryption key.

    Returns:
        str: The decrypted message.

    Raises:
        Exception: If there is an error while decrypting the message.
    """
    try:
        cipher_suite = Fernet(load_key(key_file_path))
        decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    except Exception:
        LOGGER.exception('An error occurred while decrypting the message.')
        raise
    LOGGER.debug('Decrypted message successfully.')
    return decrypted_message
