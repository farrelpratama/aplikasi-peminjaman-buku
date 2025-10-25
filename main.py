from module.auth import login_form, register_form

def main():
    show_landing_page()

    user_choice = menu_input()  
    if user_choice == '1':
        print("Anda memilih untuk register.")
        user_register = register_form()
        print(user_register)
        # Panggil fungsi register di sini
    elif user_choice == '2':
        print("Anda memilih untuk login.")
        user_login = login_form()
        print(user_login)
        # Panggil fungsi login di sini
        # Jika login gagal, tampilkan pesan kesalahan dan kembali ke landing page
        # Jika login berhasil, tampilkan menu user atau admin sesuai peran    
    elif user_choice == '3':
        print("Terima kasih telah menggunakan aplikasi kami. Sampai jumpa!")
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        main()


def menu_input():
    print("==============================")
    print("Silakan pilih menu:")
    choice = input("Masukkan pilihan Anda: ")
    return choice

def show_landing_page():
    print("==============================")
    print("  SELAMAT DATANG DI PERPUS   ")
    print("==============================")
    print("1. register")
    print("2. login")
    print("3. Keluar")

def user_menu():
    print("==============================")
    print("    MENU PEMINJAMAN BUKU      ")
    print("==============================")
    print("1. Lihat Daftar Buku")
    print("2. Ajukan Peminjaman Buku")
    print("3. Keluar")
    print("==============================")  
    print("Silakan pilih menu:")
    choice = input("Masukkan pilihan Anda: ")
    return choice

if __name__ == "__main__":
    main()