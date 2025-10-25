import json
import os

# PATH = 'data'
def load_users():
    if not os.path.exists('data/user.json'):
        with open('data/user.json', 'w') as f:
            f.write('[]')
    with open('data/user.json', 'r') as f:
        users = json.load(f)
    return users

def register_form():
    print("\n")
    print("==============================")
    print("         REGISTER             ")
    print("==============================")
    name = input("Masukkan nama Anda: ")
    email = input("Masukkan email Anda: ")
    password = input("Masukkan password Anda: ")
    confirm_password = input("Konfirmasi password Anda: ")
    if password != confirm_password:
        print("Password tidak cocok!")
        return None
    
    return {"name":name, "email":email, "password":password}

def login_form():
    print("\n")
    print("==============================")
    print("           LOGIN              ")
    print("==============================")
    email = input("Masukkan email Anda: ")
    password = input("Masukkan password Anda: ")
    return {"email":email, "password":password}

