import socket

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_public_ip():
    import requests
    public_ip = requests.get('https://api.ipify.org').text
    return public_ip

print("Local IP Address:", get_local_ip())
print("Public IP Address:", get_public_ip())