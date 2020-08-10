from iota import Iota
from iota import TryteString

HASH_TXN = "QDPWMVRFQENKFSDHKXIWNMWFHTIXQGXTGTPRSJHILXUDYTPJXLBVMFPPFDZIVIUODJWCBBEFZJGFZ9999"

api = Iota('http://node.deviceproof.org:14265')

tail_hash = HASH_TXN
bundle = api.get_bundles(tail_hash)
signature_message_fragment = str(bundle["bundles"][0][0].signature_message_fragment)

print(TryteString(signature_message_fragment).decode())
