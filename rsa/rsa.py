from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode
import binascii

def bin2hex(bin_str):
    return binascii.hexlify(bin_str)

def hex2bin(hex_str):
    return binascii.unhexlify(hex_str)

def gen_key_pair():
    key = RSA.generate(1024)
    public_key = key.publickey().exportKey('PEM').decode('ascii')
    private_key = key.exportKey('PEM').decode('ascii')

    return public_key, private_key

def encrypt_with_pub_key(pub_key, data):
    publickey = RSA.importKey(pub_key)
    encryptor = PKCS1_OAEP.new(publickey)
    # Convert data to byte and encrypt it
    encrypted = encryptor.encrypt(str.encode((data)))
    # Convert byte to hex
    encrypted = bin2hex(encrypted)
    # Convert hex to string
    encrypted = encrypted.decode('ascii')

    return encrypted

def decrypt_with_pri_key(user, data):
    # Decrypt
    private_key = ""
    decrypted = "" 
    with open("accounts/" + user + "/private.pem", 'r') as outfile:
        private_key = outfile.read()

    privatekey = RSA.importKey(private_key)
    decryptor = PKCS1_OAEP.new(privatekey)

    # Convert string to byte
    encrypted = data.encode('ascii')
    
    # Hex to bin
    encrypted = hex2bin(encrypted)
    decrypted = decryptor.decrypt(encrypted)

    return decrypted.decode()
