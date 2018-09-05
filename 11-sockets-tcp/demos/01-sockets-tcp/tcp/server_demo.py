import socket
sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)
sock
address = ('127.0.0.1', 3000)
sock.bind(address)
sock
sock.listen(1)
conn, addr = sock.accept()
conn
addr
buffer_length = 8
message_complete = False
while not message_complete:
    part = conn.recv(buffer_length)
    print(part.decode('utf8'))
    if len(part) < buffer_length:
        break
message = 'thanks for the note'
conn.sendall(message.encode('utf8'))
conn.send??
conn.sendall??
while not message_complete:
    part = conn.recv(buffer_length)
    print(part.decode('utf8'))
    if len(part) < buffer_length:
        break
conn.close()
sock.close()
history
