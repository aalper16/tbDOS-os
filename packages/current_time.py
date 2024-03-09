from datetime import datetime

def time():
    try:
        now = datetime.now()
        return now
    except:
        return "Yazılımsal hata!"

