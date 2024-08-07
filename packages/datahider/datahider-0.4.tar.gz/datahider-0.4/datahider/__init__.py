import json
from cryptography.fernet import Fernet

class DataHider:
    def __init__(self, key: str):
        """
        Creates a new DataHider. Immediately loads the private key and caches it.
        :param key: The encryption key
        """
        self.crypto = Fernet(key)

    def encrypt_and_base64(self, data: any) -> str:
        """
        Encrypts the given data and base64 encodes that encrypted blob.
        :param data: The data to be encrypted
        :return: base64 encoded, encrypted data
        """

        # serialize the data into a string
        serialized_data: str = json.dumps(data)

        # encode: tell python to interpret the string as an array of bytes
        serialized_bytes: bytes = serialized_data.encode()

        # encrypt: encrypt the data (Fernet outputs base64)
        encrypted_data: bytes = self.crypto.encrypt(serialized_bytes)

        # decode: tell python to interpret the array of bytes as utf8
        # replace: and make it truly URL safe
        return encrypted_data.decode('utf-8').replace("=", "~")

    def decrypt_base64_blob(self, encrypted_string_base64: str) -> any:
        """
        Decrypts the base64 encoded encrypted data
        :param encrypted_string_base64: The base64 encoded, encrypted data
        :return: The decrypted data
        """

        # replace: undo the URL safe transform
        # encode: tell python to interpret the string as array of bytes
        encrypted_bytes: bytes = encrypted_string_base64.replace("~", "=").encode()

        # decrypt: decrypt the data
        decrypted_bytes: bytes = self.crypto.decrypt(encrypted_bytes)

        # decode: tell python to interpret the array of bytes as utf8
        serialized_data: str = decrypted_bytes.decode('utf-8')
        data = json.loads(serialized_data)
        return data
