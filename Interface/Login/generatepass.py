import bcrypt

passw = "$2b$12$hgbTKvx8BX8Kp2xo1T.zee3j24qKdUaGTOH59RvkWhKz5chzrh76e".encode("utf-8")

password = "admin".encode("utf-8")


result = bcrypt.checkpw(password, passw) 

print(result)