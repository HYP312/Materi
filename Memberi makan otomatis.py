import time #library waktu yang nantinya akan digunakan pembagian waktu

sarapan = 7
makan_siang = 12
makan_malam = 18

while True:
    waktu_saat_ini = time.localtime() #mendefisikan waktu saat ini
    jam = waktu_saat_ini.tm_hour    #mengambil jamnya saja dalam waktu
    
    #cek waktu dengan kondisi
    if jam == sarapan:
        print("Sarapan telah tiba")
    elif jam == makan_siang:
        print("Makan Siang telah tiba")
    elif jam == makan_malam:
        print("Makan malam telah tiba")
    else:
        print("Belum waktunya makan")
    #ngecek selama 1 jam
    time.sleep(3600)