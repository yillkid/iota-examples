from iota import Iota
from config import NODE_URL

TNX_HASH = "MFXNIHJUSCFBIJCGLJGHHVD9C9VAVACOU99LZZDGITMGQGKNPWUWQVMNANBTYSGFSZTLJKYPREHYZ9999"

api = Iota(NODE_URL)
dict_txn = api.find_transactions(approvees = [TNX_HASH])

print(dict_txn['hashes'])
