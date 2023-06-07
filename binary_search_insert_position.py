def mencari_posisi_sisipan(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Contoh input
data = [2, 4, 6, 8, 10, 12, 14]
target = 7

# Mencari posisi sisipan menggunakan binary search
insert_pos = mencari_posisi_sisipan(data, target)

# Menampilkan hasil pencarian
print(f"Elemen {target} dapat disisipkan pada indeks {insert_pos} untuk menjaga daftar tetap terurut.")
