from iota import Iota
from config import NODE_URL

TAG = "BIILABS"

api = Iota(NODE_URL)
dict_txn = api.find_transactions(tags = [TAG])

print(dict_txn['hashes'])
