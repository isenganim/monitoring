import getpass
import bcrypt

password = getpass.getpass("input your password: ")
hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
print(hashed_password.decode())
