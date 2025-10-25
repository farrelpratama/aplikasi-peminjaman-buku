from module.utils import load_data, save_data

BOOK_PATH = "data/books.json"

def view_books():
    """Menampilkan daftar semua buku"""
    books = load_data(BOOK_PATH)
    if not books:
        print("\n❌ Belum ada buku terdaftar.\n")
        return

    print("\n=== DAFTAR BUKU ===")
    for b in books:
        print(f"ID: {b['id']}\nJudul: {b['judul']}\nPenulis: {b['penulis']}\nStatus: {b['status']}\n")
    print("====================\n")

def add_books():
    """Menambahkan buku baru ke daftar"""
    books = load_data(BOOK_PATH)

    id_buku = input("Masukkan ID Buku: ").strip()
    # Cek apakah ID sudah ada
    for b in books:
        if b["id"] == id_buku:
            print("❌ ID buku sudah digunakan!")
            return

    title = input("Masukkan Judul Buku: ").strip()
    author = input("Masukkan Penulis Buku: ").strip()
    stock = int(input("Masukkan jumlah buku : ").strip())

    books.append({
        "id": id_buku,
        "title": title,
        "author": author,
        "stock":stock,
        "status": "tersedia"
    })

    save_data(BOOK_PATH, books)
    print("✅ Buku berhasil ditambahkan!\n")

def delete_books():
    """Menghapus buku berdasarkan ID"""
    books = load_data(BOOK_PATH)
    if not books:
        print("Belum ada buku yang bisa dihapus.")
        return

    id_buku = input("Masukkan ID Buku yang ingin dihapus: ").strip()
    for b in books:
        if b["id"] == id_buku:
            books.remove(b)
            save_data(BOOK_PATH, books)
            print("✅ Buku berhasil dihapus!\n")
            return

    print("❌ Buku dengan ID tersebut tidak ditemukan.\n")

def edit_books():
    """Mengedit data buku (judul / penulis / status)"""
    books = load_data(BOOK_PATH)
    id_buku = input("Masukkan ID Buku yang ingin diedit: ").strip()

    for b in books:
        if b["id"] == id_buku:
            print(f"Data buku saat ini:\nJudul: {b['judul']}\nPenulis: {b['penulis']}\nStatus: {b['status']}")
            judul_baru = input("Masukkan Judul baru (kosongkan jika tidak diubah): ").strip()
            penulis_baru = input("Masukkan Penulis baru (kosongkan jika tidak diubah): ").strip()
            status_baru = input("Masukkan Status baru (tersedia/dipinjam, kosongkan jika tidak diubah): ").strip()

            if judul_baru:
                b["judul"] = judul_baru
            if penulis_baru:
                b["penulis"] = penulis_baru
            if status_baru:
                b["status"] = status_baru

            save_data(BOOK_PATH, books)
            print("✅ Data buku berhasil diperbarui!\n")
            return

    print("❌ Buku dengan ID tersebut tidak ditemukan.\n")

def search_books():
    """Mencari buku berdasarkan judul atau penulis"""
    books = load_data(BOOK_PATH)
    if not books:
        print("Belum ada buku yang bisa dicari.")
        return

    keyword = input("Masukkan judul atau penulis yang ingin dicari: ").lower()
    hasil = [b for b in books if keyword in b['judul'].lower() or keyword in b['penulis'].lower()]

    if hasil:
        print("\n=== HASIL PENCARIAN ===")
        for b in hasil:
            print(f"ID: {b['id']} | Judul: {b['judul']} | Penulis: {b['penulis']} | Status: {b['status']}")
        print("========================\n")
    else:
        print("❌ Tidak ditemukan buku yang cocok.\n")
