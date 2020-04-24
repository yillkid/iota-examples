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

def decrypt_with_pri_key(data):
    # Decrypt
    private_key = ""
    decrypted = ""
    with open("./private.pem", 'r') as outfile:
        private_key = outfile.read()

    privatekey = RSA.importKey(private_key)
    decryptor = PKCS1_OAEP.new(privatekey)

    # Convert string to byte
    encrypted = data.encode('ascii')

    # Hex to bin
    encrypted = hex2bin(encrypted)
    decrypted = decryptor.decrypt(encrypted)

    return decrypted.decode()


cyphertext = "7f4aa1ee46f5b573216fc5282b1f34269a3ac83bfe11e63d5b5053d2c7ba015ed914ffd94c173ece17f7ccbb4ed2fe287a89862f0f13324a8132fbe5585908703345e58ff8ac2a7602959462cb8029c5b28dd72f8257c8785089fe049cb5efe25d4b4752ac426cd5929c617e8db9c3071f24b5e4e1d50ff0f8405f2ce1ea6de7"

cyphertext = decrypt_with_pri_key(cyphertext)

print(cyphertext)
