import socket
socket.getaddrinfo('127.0.0.1', 3000)
infos = socket.getaddrinfo('127.0.0.1', 3000)
len(2)
len(infos)
stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
socket.getaddrinfo('127.0.0.1', 3000)
stream_info
client = socket.socket(*stream_info[:3])
client
client.connect(stream_info[-1])
message = 'This is awesome. I am a client sending data to my server'
client.sendall(message.encode('utf8'))
conn.send?
conn.send??
buffer_length = 8
message_complete = False

while not message_complete:
    part = client.recv(buffer_length)
    print(part.decode('utf8'))
    if len(part) < buffer_length:
        break
client.close()
history
