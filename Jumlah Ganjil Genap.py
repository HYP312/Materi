n = int(input("Masukan Jumlah deret: "))
genap = 0
ganjil = 0
for i in range(n):
    if i % 2 == 0:
        genap +=1
    if i % 2 != 0:
        ganjil +=1


print("Jumlah bilangan genap dalam deret tersebut adalah: ", genap)
print("Jumlah bilangan ganjil dalam deret tersebut adalah: ", ganjil)