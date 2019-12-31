import requests
import json

# header
my_headers = {"content-type": "application/json","X-IOTA-API-Version": "1"}

# parematers
my_data = {"command": "getNodeAPIConfiguration"}

# 將資料加入 POST 請求中
r = requests.post('https://node.deviceproof.org:443', data = json.dumps(my_data), headers = my_headers)
print(r.text)
