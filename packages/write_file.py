import os

def write(path, content):
    try:
        with open(f'{path}', 'w') as writeFile:
            writeFile.write(content)
        return "İşlem gerçekleştirildi"
    except:
        return "Yazılımsal hata!"
