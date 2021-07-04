## importing socket module
import socket
def hostname():
    ## getting the hostname by socket.gethostname() method
    host_name = socket.gethostname()
    print(f"Hostname: {host_name}")
    return host_name

def ipaddress():
    ## getting the hostname by socket.gethostname() method
    host_name = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(host_name)
    ## printing the hostname and ip_address
    print(f"IP Address: {ip_address}")
    return ip_address
