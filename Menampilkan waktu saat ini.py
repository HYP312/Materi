import time #memanggil library time

waktu = time.localtime()

print("Waktu saat ini adalah: ", time.strftime("%H:%M:%S", waktu))