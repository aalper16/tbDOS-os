from packages import append_file, create_file, current_time, delete_file, get_host, write_file, sys_info, process_toml, setup
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


username = input('Kullanıcı adınız: ')
password = input('Şifreniz: ')

getname = process_toml.get_data('reg/user.toml').get('name')
getpasswd = process_toml.get_data('reg/user.toml').get('password')

if username == getname and password == getpasswd:
    print('Oturum açıldı.')
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

        elif komut == 'kullanıcı_giriş':
            newname = input('Yeni kullanıcı ismi: ')
            newpasswd = input('Yeni şifre: ')
            confnewpasswd = input('Yeni şifreyi doğrulayın: ')

            if newpasswd == confnewpasswd:
                user = {
                    'name': f'{newname}',
                    'password': f'{newpasswd}'
                }
                process_toml.load_data('reg/user.toml', user)

        elif komut == 'kurulum':
            setup.start()

else:
    print('Kullanıcı bilgileri yanlış! Varsayılan isim "user" ve varsayılan şifre "user"dir.')