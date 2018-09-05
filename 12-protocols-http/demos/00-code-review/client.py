import socket
import sys

PORT = 3000

infos = socket.getaddrinfo('127.0.0.1', PORT)

stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
# for sock_data in infos:
#     if sock_data[1] == socket.SOCK_STREAM:
#         stream_info = sock_data  # 5-tuple repr of socket

# 5-tuple => (Family, Kind, Protocol, '', Endpoint)

client = socket.socket(*stream_info[:3])
# client = socket.socket(
#     stream_info[0],  # Family
#     stream_info[1],  # Kind
#     stream_info[2],  # Protocol
# )


client.connect(stream_info[-1])  # ('127.0.0.1', 3000)

message = sys.argv[1]

client.sendall(message.encode('utf8'))

buffer_length = 8

message_complete = False

server_msg = b''
while not message_complete:
    part = client.recv(buffer_length)
    server_msg += part
    if len(part) < buffer_length:
        break

server_msg = server_msg.decode('utf8')
print(server_msg)

client.close()
