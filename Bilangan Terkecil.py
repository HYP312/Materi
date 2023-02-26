n = int(input("Masukan banyak bilangan: "))
deret =[]
for i in range(n):
    a = input("Masukan angka: ")
    deret.append(int(a))

terkecil = min(deret)
print("Bilangn Terkecil adalah: ", terkecil)
