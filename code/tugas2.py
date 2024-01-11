def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def nth_prime(n):
    prime_count = 0
    candidate = 2  # Mulai dari bilangan prima pertama
    while True:
        if is_prime(candidate):
            prime_count += 1
            if prime_count == n:
                return candidate
        candidate += 1

n = int(input("Masukkan nilai n: "))
result = nth_prime(n)
print(f"Bilangan prima ke-{n} adalah {result}")
