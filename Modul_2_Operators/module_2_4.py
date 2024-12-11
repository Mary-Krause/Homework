numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_Primes = []
is_prime = True
for i in numbers:
    if i > 1:
        for j in range(2, i - 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        else:
            is_prime = True
            not_Primes.append(i)
print(f'Список с простыми числами: {primes}')
print(f'Список с сложными числами: {not_Primes}')
