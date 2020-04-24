from Crypto.PublicKey import RSA

def gen_key_pair():
    key = RSA.generate(1024)
    public_key = key.publickey().exportKey('PEM').decode('ascii')
    private_key = key.exportKey('PEM').decode('ascii')

    return public_key, private_key

pub_key, pri_key = gen_key_pair()
with open("./private.pem", 'w') as outfile:
    outfile.write(pri_key)

with open("./public.txt", 'w') as outfile:
    outfile.write(pub_key)
