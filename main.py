from packages import append_file, create_file, current_time, delete_file, get_host, write_file, sys_info
from colorama import *
import os

print("tbDOS starting at: "+get_host.get_host())
print('İşletim sistemi: '+sys_info.get_os())
print('İşletim sistemi versiyonu: '+sys_info.get_version())
print('Makine tipi: '+sys_info.get_type())
print('Makine işlemcisi: '+sys_info.get_processor())
print('Python sürümü: '+sys_info.get_python())
print('RAM kapasitesi: '+sys_info.get_ram()+' MB')
print('\n \n')

while True:
    komut = input('Kullanıcı komutu: ')

    if komut == 'zaman':
        print(current_time.time())

    elif komut == 'dosya':
        islem = input('İşlem giriniz:')
        if islem == 'oluştur':
            isim = input('Dosya ismi: ')
            create_file.make(isim)
        elif islem == 'sil':
            isim = input('Dosya ismi: ')
            delete_file.delete(isim)
        elif islem == 'yaz':
            isim = input('Dosya ismi: ')
            icerik = input('Dosya içeriği: ')
            write_file.write(isim, icerik)
        elif islem == 'ekle':
            isim = input('Dosya ismi: ')
            ekle = input('Ekle: ')
            append_file.append(isim, ekle)

    elif komut == 'ip':
        print(get_host.get_host())

    elif komut == 'sistem_bilgisi':
        print('İşletim sistemi: '+sys_info.get_os())
        print('İşletim sistemi versiyonu: '+sys_info.get_version())
        print('Makine tipi: '+sys_info.get_type())
        print('Makine işlemcisi: '+sys_info.get_processor())
        print('Python sürümü: '+sys_info.get_python())
        print('RAM kapasitesi: '+sys_info.get_ram()+' MB')

    elif komut == 'temiz':
        os.system('cls')