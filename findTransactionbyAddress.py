from iota import Iota
from config import NODE_URL

ADDRESS = "SSEFNDKCIFHOFFCA9IXNBEQIYUQEXHIIHQIOWIEEAFBENHVS9ZASLWKPZNQFSTUCQXJAOKJDDHVXVXGUBBA9CFNYXW"

api = Iota(NODE_URL)
dict_txn = api.find_transactions(addresses = [ADDRESS])

print(dict_txn['hashes'])
