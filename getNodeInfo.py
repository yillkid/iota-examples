from iota import Iota
from config import NODE_URL
import json

api = Iota(NODE_URL)
print(api.get_node_info())
