n = int(input("Masukan banyak bilangan: "))
deret =[]
for i in range(n):
    a = input("Masukan angka: ")
    deret.append(int(a))

terbesar = max(deret)
print("Bilangn terbesar adalah: ", terbesar)
