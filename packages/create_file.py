import os

def make(arg):
    try:
        os.mkdir(arg)
        return "İşlem gerçekleşirildi"
    except:
        return "Yazılımsal hata!"
