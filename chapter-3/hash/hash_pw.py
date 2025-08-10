import hashlib
import data as data_pw_user

password = data_pw_user.data["password"]

hashed = hashlib.sha256(password.encode()).hexdigest()  

data_pw_user.data["password"] = hashed

print("Hashed password:", data_pw_user.data["password"])
print("Original password:", password)
