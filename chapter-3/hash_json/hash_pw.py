import hashlib
import data

hashed_password = hashlib.sha256(data.get_data["password"].encode()).hexdigest()
print(hashed_password)
