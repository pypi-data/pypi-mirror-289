from cryptography.fernet import Fernet
import os
import logging

LOGGER = logging.getLogger(__name__)

def generate_key(file_path):
    try:
        key = Fernet.generate_key()
        with open(file_path, "wb") as key_file:
            key_file.write(key)
    except Exception:
        LOGGER.exception(f"An error occured while generating key file '{file_path}'.")
        raise
    LOGGER.debug(f"Generated key file '{file_path}'.")


def load_key(file_path: str):
    try:
        with open(file_path, "rb") as key_file:
            key = key_file.read()
        
    except Exception:
        LOGGER.exception(f"An error occured while loading key file '{file_path}'.")
        raise
    LOGGER.debug(f"Loaded key file '{file_path}'.")
    return key
    

def encrypt(message, key_file_path):
    try:
        cipher_suite = Fernet(load_key(key_file_path))
        encrypted_message = cipher_suite.encrypt(message.encode())
    except Exception:
        LOGGER.exception('An error occured while decrypting message.')
        raise
    LOGGER.debug('Encrypted message successfully.')
    return encrypted_message

def decrypt(encrypted_message, key_file_path):
    try:
        cipher_suite = Fernet(load_key(key_file_path))
        decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    except Exception:
        LOGGER.exception('An error occured while decrypting message.')
        raise
    LOGGER.debug('Decrypted message successfully.')
    return decrypted_message


