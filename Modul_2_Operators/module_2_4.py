from itertools import count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_Primes = []
is_prime = 0
count = 0
for i in numbers:
    for j in range(2, 15):
        if i % j == 0:
            count += 1
        elif count > 1:
            not_Primes.append(i)
        else:primes.append(i)
print(primes)
print(not_Primes)

   # if i % 2 == 0:
     #   not_Primes.append(i)
     #   print(not_Primes)
