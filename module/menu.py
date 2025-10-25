from module.books import view_books, add_books, edit_books, delete_books, search_books 
from module.loans import borrow_book

def user_menu(user):
    """Menu utama untuk user"""
    while True:
        print("==============================")
        print("    MENU PEMINJAMAN BUKU      ")
        print("==============================")
        print("1. Lihat Daftar Buku")
        print("2. Ajukan Peminjaman Buku")
        print("3. Keluar")
        print("==============================")

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            view_books()
        elif pilihan == "2":
            borrow_book(user) 
        elif pilihan == "3":
            print("Kembali ke menu utama...\n")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi!\n")


def admin_menu():
    """Menu utama untuk admin"""
    while True:
        print("==============================")
        print("       MENU ADMIN BUKU        ")
        print("==============================")
        print("1. Lihat Daftar Buku")
        print("2. Tambah Buku")
        print("3. Edit Buku")
        print("4. Hapus Buku")
        print("5. Cari Buku")
        print("6. Kembali ke Menu Utama")
        print("==============================")
        
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            view_books()
        elif pilihan == "2":
            add_books()
        elif pilihan == "3":
            edit_books()
        elif pilihan == "4":
            delete_books()
        elif pilihan == "5":
            search_books()
        elif pilihan == "6":
            print("Kembali ke menu utama...\n")
            
        
        else:
            print("❌ Pilihan tidak valid, coba lagi!\n")


