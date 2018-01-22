import socket
x=0
serverUDP_IP = "127.0.0.1"
serverUDP_PORT = 5023

clientUDP_IP = "127.0.0.2"
clientUDP_PORT = 6023


sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP

sock.bind((clientUDP_IP, clientUDP_PORT))
while True:
    
       
    MESSAGE =input("Enter Your Value: ")
    strMESSAGE=str(MESSAGE)

    print "UDP target IP:", serverUDP_IP
    print "UDP target port:", serverUDP_PORT
    print "message:", strMESSAGE
  
    sock.sendto(strMESSAGE, (serverUDP_IP, serverUDP_PORT))

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    
    

  
