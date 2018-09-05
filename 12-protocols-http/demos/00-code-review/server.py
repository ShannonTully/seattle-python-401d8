from datetime import datetime
import socket

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)

PORT = 3000

address = ('127.0.0.1', PORT)

sock.bind(address)

try:
    sock.listen(1)

    print('--- Starting server on port {} at {} ---'.format(PORT, datetime.now().strftime('%H:%M:%S %d-%m-%y')))
    conn, addr = sock.accept()
    # conn == <Socket ...>
    # addr = ('127.0.0.1, 5678)
    import pdb; pdb.set_trace()

    buffer_length = 8

    message_complete = False

    message = b''
    while not message_complete:
        part = conn.recv(buffer_length)
        message += part

        if len(part) < buffer_length:
            break

    message = message.decode('utf8')
    print('{} Echoed: {}'.format(datetime.now().strftime('%H:%M:%S %d-%m-%y'), message))

    conn.sendall(message.encode('utf8'))

except KeyboardInterrupt:
    try:
        conn.close()
    except NameError:
        pass

    sock.close()
    print('--- Stopping server on port {} at {} ---'.format(PORT, datetime.now().strftime('%H:%M:%S %d-%m-%y')))

conn.close()
sock.close()
print('--- Stopping server on port {} at {} ---'.format(PORT, datetime.now().strftime('%H:%M:%S %d-%m-%y')))
