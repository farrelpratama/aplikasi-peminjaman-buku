from module.utils import load_data, save_data

USER_FILE = "data/users.json"

def register_form():
    users = load_data(USER_FILE)
    print("\n")
    print("==============================")
    print("         REGISTER             ")
    print("==============================")
    name = input("Masukkan nama Anda: ")
    email = input("Masukkan email Anda: ")
    if users:
        for user in users:
            # Cek apakah email sudah terdaftar
            if user["email"] == email:
                print("❌ Email sudah terdaftar!")
                return None
    
    password = input("Masukkan password Anda: ")
    confirm_password = input("Konfirmasi password Anda: ")
    if password != confirm_password:
        print("Password tidak cocok!")
        return None
    
    default_role = "user"
    new_user = {
        "name": name,
        "role": default_role,
        "email": email,
        "password": password
    }

    users.append(new_user)
    save_data(USER_FILE, users)
    print("✅ Registrasi berhasil!\n")
    return new_user

def login_form():
    users = load_data(USER_FILE)
    print("\n")
    print("==============================") 
    print("           LOGIN              ")
    print("==============================")
    email = input("Masukkan email Anda: ")
    password = input("Masukkan password Anda: ")
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("✅ Login berhasil!\n")
            return user
    
    print("❌ Email atau password salah!\n")
    return None

