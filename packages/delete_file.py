import os 

def delete(path):
    try:
        os.system('del '+path)
        return "İşlem gerçekleştirildi"
    except:
        return "Yazılımsal hata!"
