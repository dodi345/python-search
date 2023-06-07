def temukan_nomor_hp(name, phone_book):
    for entry in phone_book:
        if entry[0] == name:
            return entry[1]
    return None

# Tabel buku telepon
phone_book = [
    ["John Doe", "081234567890"],
    ["Jane Smith", "089876543210"],
    ["Michael Johnson", "087811223344"],
    ["Emily Davis", "082122232425"]
]

# Mencari nomor telepon Jane menggunakan sequential search
name = "Jane Smith"
phone_number = temukan_nomor_hp(name, phone_book)

# Menampilkan hasil pencarian
if phone_number:
    print(f"Nomor telepon {name}: {phone_number}")
else:
    print(f"Tidak ditemukan nomor telepon untuk {name}")
