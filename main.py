from module.auth import login_form, register_form
from module.menu import user_menu, admin_menu

def main():
    show_landing_page()

    user_choice = menu_input()  
    if user_choice == '1':
        print("Anda memilih untuk register.")
        register_form()
        # Panggil fungsi register di sini
    elif user_choice == '2':
        print("Anda memilih untuk login.")
        user_login = login_form()
        if user_login['role'] == 'admin':
            admin_menu()
        else:
            user_menu(user_login) 
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


if __name__ == "__main__":
    main()