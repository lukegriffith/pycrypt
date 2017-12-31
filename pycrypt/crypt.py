from cryptography.fernet import Fernet
from base64 import b64encode
import hashlib


def generate_key(symmetric_key):
    
    string_64 = b64encode(symmetric_key.encode())
    
    md5hash = hashlib.new('md5')

    md5hash.update(string_64)

    key = md5hash.hexdigest()

    key_64 = b64encode(key.encode())

    f = Fernet(key_64)

    return f


def encrypt(fernet_key, string):
     
     token = fernet_key.encrypt(string.encode())
     return token

def decrypt(fernet_key, token):

    return fernet_key.decrypt(token)