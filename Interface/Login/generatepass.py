import bcrypt

password = "hoangduy2003"

hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

print(hashed_password.decode())

