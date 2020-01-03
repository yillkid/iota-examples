import requests
import json

# header
my_headers = {"content-type": "application/json","X-IOTA-API-Version": "1"}

# parematers
my_data = {"command": "wereAddressesSpentFrom", "addresses": ["MVSHIJHYLFDDPPKPT9MFDDUDZ9NMAUJZHLKJMGGSASKPKWCCBEYYWYGSTBDTHVOQFPNNKEFYBKECZKFAA", "SSEFNDKCIFHOFFCA9IXNBEQIYUQEXHIIHQIOWIEEAFBENHVS9ZASLWKPZNQFSTUCQXJAOKJDDHVXVXGUB"]}

# POST
r = requests.post('https://node.deviceproof.org:443', data = json.dumps(my_data), headers = my_headers)
print(r.text)
