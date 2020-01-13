import rsa
from base64 import b64encode, b64decode

msg1 = "Hello Tony, I am Jarvis!"
msg2 = "Hello Toni, I am Jarvis!"
keysize = 2048
(public, private) = rsa.newkeys(keysize)

encrypted = b64encode(rsa.encrypt(msg1.encode(), public))
decrypted = rsa.decrypt(b64decode(encrypted), private)
signature = b64encode(rsa.sign(msg1.encode(), private, "SHA-512"))
verify = rsa.verify(msg1.encode(), b64decode(signature), public)

print(private.exportKey('PEM'))
print(public.exportKey('PEM'))
print("Encrypted: " + encrypted.decode())
print("Decrypted: '%s'" % decrypted)
print("Signature: " + signature.decode())
print("Verify: %s" % verify)
rsa.verify(msg2.encode(), b64decode(signature), public)
