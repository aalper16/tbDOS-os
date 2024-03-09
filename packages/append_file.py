import os

def append(path, content):
    try:
        with open(f'{path}', 'a') as appendFile:
            appendFile.write(content)
        return "İşlem gerçekleştirildi"
    except:
        return "Yazılımsal hata!"
