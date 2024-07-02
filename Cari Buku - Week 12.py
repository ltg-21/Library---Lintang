print("Selamat datang di Perpustakaan. Silahkan input data-data yang diminta. ")
# Daftar buku perpustakaan (data buku)
library = []

def add_book():
    # Fungsi untuk menambahkan buku ke dalam perpustakaan
    title = input("Masukkan judul buku: ")
    author = input("Masukkan nama penulis: ")
    year = input("Masukkan tahun terbit: ")

    book = {"title": title, "author": author, "year": year}
    library.append(book)
    print(f"Buku '{title}' berhasil ditambahkan ke perpustakaan!")

def search_books(keyword):
    # Fungsi untuk mencari buku berdasarkan kata kunci judul, penulis, atau tahun
    results = []
    for book in library:
        if (keyword.lower() in book["title"].lower() or
            keyword.lower() in book["author"].lower() or
            keyword.lower() in book["year"].lower()):
            results.append(book)
    return results

def display_books(books):
    # Fungsi untuk menampilkan daftar buku
    if not books:
        print("Tidak ada buku yang ditemukan dengan kata kunci tersebut.")
    else:
        print("Buku yang ditemukan:")
        for book in books:
            print(f"Judul: {book['title']}, Penulis: {book['author']}, Tahun: {book['year']}")

def main():
    while True:
        print("\nMenu Perpustakaan:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Keluar")
        choice = input("Pilih menu: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            keyword = input("Masukkan buku yang ingin dicari (judul/penulis/tahun terbit): ")
            results = search_books(keyword)
            display_books(results)
        elif choice == '3':
            print("Terima kasih telah menggunakan perpustakaan!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
