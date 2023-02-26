import math #library untuk matematika, digunakan pada operasi akar

# Definisikan konstanta c
c = 3.00 * 10**8

# Masukkan nilai v (kecepatan)
v = float(input("Masukkan nilai v (kecepatan) dalam m/s: "))

# Hitung dilatasi waktu
dilatasi_waktu = 1/math.sqrt(1-(v**2/c**2))

# Tampilkan hasil
print("Dilatasi Waktu anda adalah", dilatasi_waktu)