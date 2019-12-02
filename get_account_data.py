import json
from iota import Iota
from config import SEED, NODE_URL

# Iota instance
api = Iota(NODE_URL, SEED)

# Generate new address
print(api.get_account_data())
