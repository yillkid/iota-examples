from iota import Iota
from config import NODE_URL
import json

TXN_HASH = "CLTQFSGD9KJHZPUOJEMKWDZRGMKUHAAGAXFWXNJNZRKGWCXBFNBIW9SZZ9LPWGGNOBHOQWAVEPEH99999"

api = Iota(NODE_URL)
print(api.check_consistency([TXN_HASH]))
