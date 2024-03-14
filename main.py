from packages import append_file, create_file, current_time, delete_file, get_host, write_file, sys_info, process_toml, setup, process
from colorama import *
import os

print(Fore.GREEN+"tbDOS starting at: "+get_host.get_host())
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
    print(Fore.BLUE+'Oturum açıldı.')
    time = current_time.time()
    log = {
        'log': [{
        'msg': 'logged in',
        'time': f'{time}',
        '----------': '----------'
        }]
    }
    process.post(log)
    while True:
        print(Fore.RED+"|<-komut@"+getname)
        print(Fore.WHITE+"|")
        komut = input(Fore.WHITE+"|--> ")

        if komut == 'zaman':
            print(current_time.time())
            time = current_time.time()
            com = {
                'log': [{
                'msg': 'zaman',
                'time': f'{time}',
                '----------': '----------'
                }]
            }
            process.post(com)

        elif komut == 'dosya':
            time = current_time.time()
            com = {
                'log': [{
                'msg': 'dosya',
                'time': f'{time}',
                '----------': '----------'
                }]
            }
            process.post(com)
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
            time = current_time.time()
            com = {
                'log': [{
                'msg': 'ip',
                'time': f'{time}',
                '----------': '----------'
                }]
            }
            process.post(com)
            print(get_host.get_host())

        elif komut == 'sistem bilgisi':
            time = current_time.time()
            com= {
                'log': [{
                'msg': 'sistem bilgisi',
                'time': f'{time}',
                '----------': '----------'
                }]
            }
            process.post(com)
            print('İşletim sistemi: '+sys_info.get_os())
            print('İşletim sistemi versiyonu: '+sys_info.get_version())
            print('Makine tipi: '+sys_info.get_type())
            print('Makine işlemcisi: '+sys_info.get_processor())
            print('Python sürümü: '+sys_info.get_python())
            print('RAM kapasitesi: '+sys_info.get_ram()+' MB')

        elif komut == 'temiz':
            time = current_time.time()
            com = {
                'log': [{
                'msg': 'temiz',
                'time': f'{time}',
                '----------': '----------'
                }]
            }
            process.post(com)
            os.system('cls')

        elif komut == 'kullanıcı giriş':
            time = current_time.time()
            com = {
                'log': [{
                'msg': 'kullanıcı giriş',
                'time': f'{time}',
                '----------': '----------'
                }]
            }
            process.post(com)
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
            time = current_time.time()
            com = {
                    'log': [{
                    'msg': 'kurulum',
                    'time': f'{time}',
                    '----------': '----------'
                    }]
                }
            process.post(com)
            setup.start()

else:
    time = current_time.time()
    com = {
        'log': [{
        'msg': 'wrong login',
        'time': f'{time}',
        '----------': '----------'
        }]
    }
    process.post(com)
    print('Kullanıcı bilgileri yanlış! Varsayılan isim "user" ve varsayılan şifre "user"dir.')