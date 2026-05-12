import hashlib

password = "mypassword"

hashed = hashlib.md5(password.encode())

print(hashed.hexdigest())
