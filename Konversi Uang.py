# Program Konversi Uang

# Input
uang = int(input("Masukkan jumlah uang: "))

# Proses
ribuan = uang // 1000
sisa_ribuan = uang % 1000

ratusan = sisa_ribuan // 100
sisa_ratusan = sisa_ribuan % 100

puluhan = sisa_ratusan // 10
sisa_puluhan = sisa_ratusan % 10

satuan = sisa_puluhan

# Output
print("Uang dalam bentuk ribuan:", ribuan)
print("Uang dalam bentuk ratusan:", ratusan)
print("Uang dalam bentuk puluhan:", puluhan)
print("Uang dalam bentuk satuan:", satuan)