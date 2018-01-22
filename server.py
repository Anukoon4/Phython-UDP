import socket

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

serverUDP_IP = "127.0.0.1"
serverUDP_PORT = 5023

clientUDP_IP = "127.0.0.2"
clientUDP_PORT = 6023

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((serverUDP_IP, serverUDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    intData = int(data)
    var =factorial(intData)
    print "Factorial is", var
    strVar =str(var)

    sock.sendto(strVar, (clientUDP_IP, clientUDP_PORT))


