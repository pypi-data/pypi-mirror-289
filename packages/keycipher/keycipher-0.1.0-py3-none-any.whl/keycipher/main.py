import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


# Utility function to convert bytes to a hex string
def bytes_to_hex(b):
    return b.hex()


# Utility function to convert a hex string to bytes
def hex_to_bytes(h):
    return bytes.fromhex(h)


# Hash the string to produce a key of correct length
def create_key_from_string(key_string):
    # Encode the key string and hash it using SHA-256
    key_bytes = key_string.encode("utf-8")
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(key_bytes)
    key_hash = digest.finalize()

    # Derive a key from the hash
    return key_hash


# Encrypt function
def encrypt_data(plain_text, key_string):
    key = create_key_from_string(key_string)

    # Encode the plaintext
    data = plain_text.encode("utf-8")

    # Generate a random IV
    iv = os.urandom(12)

    # Create a cipher object and encrypt the data
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    cipher_text = encryptor.update(data) + encryptor.finalize()

    # Get the tag
    tag = encryptor.tag

    return {
        "iv": bytes_to_hex(iv),
        "cipherText": bytes_to_hex(cipher_text),
        "tag": bytes_to_hex(tag),
    }


# Decrypt function
def decrypt_data(encrypted_data, key_string):
    key = create_key_from_string(key_string)

    iv = hex_to_bytes(encrypted_data["iv"])
    cipher_text = hex_to_bytes(encrypted_data["cipherText"])
    tag = hex_to_bytes(encrypted_data["tag"])

    # Create a cipher object and decrypt the data
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(cipher_text) + decryptor.finalize()

    return decrypted_data.decode("utf-8")
