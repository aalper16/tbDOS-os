import socket

def get_host():
    try:
        name = socket.gethostname()
        address = socket.gethostbyname(name)
        return address
    except:
        return "Adres alınamadı!"
    
print(get_host())