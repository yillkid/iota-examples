import json
from iota import Iota
from config import SEED, NODE_URL

# Iota instance
api = Iota(NODE_URL, SEED)

# Generate new address
dict_addr = api.get_new_addresses(count = None, index = None)

print("New address: " + str(dict_addr['addresses']))
