def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Perulangan untuk memindahkan elemen terbesar ke akhir daftar
        for j in range(0, n-i-1):
            # Bandingkan elemen saat ini dengan elemen berikutnya
            if arr[j] > arr[j+1]:
                # Jika elemen saat ini lebih besar, tukar posisinya
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Daftar nilai ujian siswa
nilai = [78, 65, 90, 82, 70]

# Panggil fungsi bubble_sort untuk mengurutkan daftar nilai
bubble_sort(nilai)

# Tampilkan daftar nilai setelah diurutkan
print("Daftar nilai setelah diurutkan:")
print(nilai)
