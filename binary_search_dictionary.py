def mencari_definisi_biner(word, dictionary):
    left = 0
    right = len(dictionary) - 1

    while left <= right:
        mid = (left + right) // 2
        current_word, definition = dictionary[mid]

        if current_word == word:
            return definition
        elif current_word < word:
            left = mid + 1
        else:
            right = mid - 1

    return None

# Kamus ajaib
dictionary = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

# Kata yang ingin dicari definisinya
word = "Cat"

# Mencari definisi kata menggunakan binary search
definition = mencari_definisi_biner(word, dictionary)

# Menampilkan hasil pencarian
if definition:
    print(f"Definisi kata '{word}': {definition}")
else:
    print(f"Tidak ditemukan definisi untuk kata '{word}'")
