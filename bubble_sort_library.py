def bubble_sort_books(arr):
    n = len(arr)
    for i in range(n):
        # Perulangan untuk memindahkan buku dengan jumlah halaman terkecil ke akhir daftar
        for j in range(0, n-i-1):
            # Bandingkan jumlah halaman buku saat ini dengan jumlah halaman buku berikutnya
            if arr[j][2] > arr[j+1][2]:
                # Jika jumlah halaman buku saat ini lebih besar, tukar posisinya
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Daftar buku yang perlu diurutkan
books = [
    [1, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 320],
    [2, "To Kill a Mockingbird", "Harper Lee", 281],
    [3, "The Great Gatsby", "F. Scott Fitzgerald", 180],
    [4, "Pride and Prejudice", "Jane Austen", 432],
    [5, "1984", "George Orwell", 328]
]

# Panggil fungsi bubble_sort_books untuk mengurutkan daftar buku berdasarkan jumlah halaman
bubble_sort_books(books)

# Tampilkan daftar buku setelah diurutkan berdasarkan jumlah halaman secara ascending
print("Daftar buku setelah diurutkan berdasarkan jumlah halaman secara ascending:")
print("No.   Judul Buku                            Penulis                 Jumlah Halaman")
for book in books:
    print(f"{book[0]:<5} {book[1]:<36} {book[2]:<23} {book[3]}")
