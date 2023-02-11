import socket


def is_connected():
    try:
        # Try to connect to google.com
        host = socket.gethostbyname("www.google.com")
        socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False
