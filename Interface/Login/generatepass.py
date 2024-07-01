import bcrypt

password = "duyhoang1711"

hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

print(hashed_password.decode())

