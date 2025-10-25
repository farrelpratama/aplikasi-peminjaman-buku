from module.utils import load_data, save_data
from datetime import datetime

BOOK_FILE = "data/books.json"
LOAN_FILE = "data/loans.json"

def borrow_book(user):
    books = load_data(BOOK_FILE)
    transactions = load_data(LOAN_FILE)

    print("\n=== PINJAM BUKU ===")
    for idx, book in enumerate(books, start=1):
        print(f"{idx}. {book['title']} - Stok: {book['stock']}")

    idx = int(input("Pilih nomor buku: ")) - 1

    if 0 <= idx < len(books):
        if books[idx]["stock"] > 0:
            books[idx]["stock"] -= 1
            new_tx = {
                "username": user["username"],
                "book": books[idx]["title"],
                "borrow_date": datetime.now().strftime("%Y-%m-%d"),
                "return_date": None
            }
            transactions.append(new_tx)
            save_data(BOOK_FILE, books)
            save_data(LOAN_FILE, transactions)
            print("Buku berhasil dipinjam!")
        else:
            print("Stok buku habis.")
    else:
        print("Pilihan tidak valid.")

def return_book(user):
    transactions = load_data(LOAN_FILE)
    user_tx = [tx for tx in transactions if tx["username"] == user["username"] and tx["return_date"] is None]

    if not user_tx:
        print("Tidak ada buku yang sedang dipinjam.")
        return

    print("\n=== DAFTAR PEMINJAMAN AKTIF ===")
    for idx, tx in enumerate(user_tx, start=1):
        print(f"{idx}. {tx['book']} (Dipinjam: {tx['borrow_date']})")

    idx = int(input("Pilih buku yang ingin dikembalikan: ")) - 1
    if 0 <= idx < len(user_tx):
        user_tx[idx]["return_date"] = datetime.now().strftime("%Y-%m-%d")
        save_data(LOAN_FILE, transactions)
        print("Buku berhasil dikembalikan!")
    else:
        print("Pilihan tidak valid.")

def view_transactions():
    transactions = load_data(LOAN_FILE)
    print("\n=== DATA TRANSAKSI ===")
    for tx in transactions:
        print(f"{tx['username']} - {tx['book']} | Pinjam: {tx['borrow_date']} | Kembali: {tx['return_date']}")
