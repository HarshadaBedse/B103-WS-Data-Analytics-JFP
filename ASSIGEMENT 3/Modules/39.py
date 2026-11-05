import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(8):
    password += random.choice(characters)

print("Password:", password)



#Password: u2E:c5%\