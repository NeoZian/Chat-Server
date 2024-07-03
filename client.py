import socket

# def inClient():
#     port = 3333
#     CHUNK = 65535
#
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
#     #instead of explicitly binding the socket, we can let the os to do it
#     #empheral ports
#     #os will bind this for us
#
#     hostname = '127.0.0.1'
#
#     while True:
#         s.connect(hostname, port)
#         message = input("Type message: ")
#         data = message.encode('ascii')
#         s.send(data)
#
#         data = s.recv(CHUNK)
#         text = data.decode('ascii')
#         print(f"from server: {text}")

#========================================

port = 3333
CHUNK = 65535

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #instead of explicitly binding the socket, we can let the os to do it
    #empheral ports
    #os will bind this for us

hostname = '127.0.0.1'

while True:

    s.connect((hostname,port))
    message = input("Type message: ")
    data = message.encode('ascii')
    s.send(data)

    data = s.recv(CHUNK)
    text = data.decode('ascii')
    print(f"from server: {text}")
