import socket
import requests
import re


def is_connected():
    try:
        # Try to connect to google.com
        host = socket.gethostbyname("www.google.com")
        socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False


def get_public_ip():
    if is_connected():
        response = requests.get("https://api.ipify.org")
        if response.status_code == 200:
            return response.text.strip()
    return None


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        return s.getsockname()[0]
    except:
        return None
    finally:
        s.close()
