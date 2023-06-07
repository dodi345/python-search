def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes

# Daftar bilangan
numbers = [7, 10, 13, 6, 17, 22, 19]

# Mencari bilangan prima dalam daftar menggunakan sequential search
prime_numbers = find_primes(numbers)

# Menampilkan bilangan prima yang ditemukan
print("Bilangan prima yang ditemukan:")
for prime in prime_numbers:
    print(prime)
