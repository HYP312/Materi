n = int(input("Masukan jumlah To do listmu: "))

list = [] #tempat untuk menyimpan to do listmu

#meminta daftar to do list darimu
for i in range(n):
    a = input("Masukan daftar to do listmu(Tambahkan nomor untuk mempermudah): ")
    list.append(str(a))

#untuk menampilkan to do listmu
print("Daftar To Do Listmu:")
for item in list:
    print(item)