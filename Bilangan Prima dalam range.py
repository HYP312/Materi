n = int(input("Masukan jumlah deret: "))
prime = 2
while prime < n:
    for i in range(2,prime):
        if (prime % i) == 0:
            break
    else:
        print(prime)
    prime += 1
