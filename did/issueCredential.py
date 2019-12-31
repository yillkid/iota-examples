from deps.send_transfer import send_transfer

file_issuer = open("credentials/new_credentials.json", "r")
content = file_issuer.read()
file_issuer.close()

print(send_transfer(content))
