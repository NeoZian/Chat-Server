import socket


# def initialization():
#     port = 3333
#     CHUNK = 65535
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creating socket object
#     #socket.socket(family, type)
#     #AF_NET: familyof ipv4
#     #SOCK_DGRAM : UDP,  and SOCK_STREAM  is for TCP
#     print(s)
#
#
#     hostname = '127.0.0.1'
#     s.bind((hostname, port))
#
#     print(f"server is live on : {s.getsockname()}")
#
#     #running this server infinitely
#
#     while True:
#         data, clientAdd = s.recvfrom(CHUNK)
#         message = data.decode('ascii')  #data by default travels in bytes
#         print(f"jewel says: How rya doin? message: {message}")
#         message_send = input("Reply: ")
#         data = message_send.encode('ascii')
#         s.sendto(data, clientAdd)  #sending the data to the ip address that sent me data

#...............................

port = 3333
CHUNK = 65535
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creating socket object
    #socket.socket(family, type)
    #AF_NET: familyof ipv4
    #SOCK_DGRAM : UDP,  and SOCK_STREAM  is for TCP
print(s)


hostname = '127.0.0.1'
s.bind((hostname, port))

print(f"server is live on : {s.getsockname()}")

    #running this server infinitely

while True:
    data, clientAdd = s.recvfrom(CHUNK)
    message = data.decode('ascii')  #data by default travels in bytes
    print(f"jewel says: How rya doin? message: {message}")
    message_send = input("Reply: ")
    data = message_send.encode('ascii')
    s.sendto(data, clientAdd)  #sending the data to the ip address that sent me data
