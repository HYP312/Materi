import time #library waktu yang nantinya akan digunakan pembagian waktu

Belajar = int(input("Masukan jam belajarmu: "))


while True:
    waktu_saat_ini = time.localtime() #mendefisikan waktu saat ini
    jam = waktu_saat_ini.tm_hour    #mengambil jamnya saja dalam waktu
    
    #cek waktu dengan kondisi
    if jam == Belajar:
        for i in range(100): #melakukan spam untuk belajar sebanyak index 100
            print("WAKTUNYA BELAJAR")
    else:
        print("Belum waktunya makan")
    #ngecek selama 1 jam
    time.sleep(3600)