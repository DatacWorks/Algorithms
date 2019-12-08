is_prime = []
not_prime = []
for n in range(2, 18):
    for x in range(2, n):
        print(f" {n} % {x} = {n % x}")
        if n % x == 0:
            not_prime.append(n)
            break
    else:
        print(f" {n} is a prime")
        is_prime.append(n)

print(f"{is_prime} Primes")
print(f"{not_prime} not primes")


