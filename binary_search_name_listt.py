import os
def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high)//2
        
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


names = ['alice', 'bob', 'charlie', 'david', 'emma', 'frank', 'george']

os.system("clear")
target_name = input("masukan nama yang ingin dicari: ")
index = binary_search(names, target_name)

if index != -1:
    print(f"nama ditemukan pada indeks {index}")
else:
    print("nama tidak ditemukan")
