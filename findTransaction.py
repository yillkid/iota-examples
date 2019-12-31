from iota import Iota
from config import NODE_URL

TXN_BUNDLE = "YKIMBDFFYFDRFTEXGFGZYFKCPTRTCDLJCHUWJTXRJRQQGHEVOZKZYOPCO9LAGKXYWRJVWKWTVGCJZNSSA"

api = Iota(NODE_URL)
dict_txn = api.find_transactions(bundles = [TXN_BUNDLE])

print(dict_txn['hashes'])
