def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Cari indeks elemen terkecil yang belum diurutkan
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Tukar elemen terkecil dengan elemen pertama dalam sisa daftar yang belum diurutkan
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Daftar angka yang dimiliki Andi
angka = [9, 5, 3, 8, 2]

# Panggil fungsi selection_sort untuk mengurutkan daftar angka
selection_sort(angka)

# Tampilkan daftar angka setelah diurutkan
print("Daftar angka setelah diurutkan:",angka)