import requests
import json

# header
my_headers = {"content-type": "application/json","X-IOTA-API-Version": "1"}

# parematers
my_data = {"command": "removeNeighbors", "uris": ["tcp://node1.puyuma.org:15600"]}

# POST
r = requests.post('http://127.0.0.1:14265', data = json.dumps(my_data), headers = my_headers)
print(r.text)
