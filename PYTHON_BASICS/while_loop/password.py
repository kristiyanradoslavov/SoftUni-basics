username = input()
password = input()
user_password = input()

while password != user_password:
    user_password = input()

print(f"Welcome {username}!")