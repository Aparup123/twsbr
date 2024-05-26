import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.0.125', 10000)

while True:
    message = "Hello server" 
    sock.sendto(message.encode(), server_address)
    time.sleep(1)

