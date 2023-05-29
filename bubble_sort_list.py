def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        # Perulangan untuk memindahkan elemen terbesar ke akhir daftar
        for j in range(0, n-i-1):
            # Bandingkan elemen saat ini dengan elemen berikutnya
            if arr[j] < arr[j+1]:
                # Jika elemen saat ini lebih kecil, tukar posisinya
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Daftar angka yang ingin diurutkan
angka = [42, 19, 33, 8, 55]

# Panggil fungsi bubble_sort_descending untuk mengurutkan daftar angka
bubble_sort_desc(angka)

# Tampilkan daftar angka setelah diurutkan secara descending
print("Daftar angka setelah diurutkan secara descending:")
print(angka)
