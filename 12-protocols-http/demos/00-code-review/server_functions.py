from datetime import datetime
import socket


PORT = 3000


def server_setup():
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP)

    address = ('127.0.0.1', PORT)

    sock.bind(address)
    sock.listen(1)
    print('--- Starting server on port {} at {} ---'.format(
        PORT, datetime.now().strftime('%H:%M:%S %d-%m-%y')))
    return sock


def start_server():
    try:
        sock = server_setup()
        conn, addr = sock.accept()

        # conn == <Socket ...>
        # addr = ('127.0.0.1, 5678)

        # import pdb; pdb.set_trace()

        buffer_length = 8

        message_complete = False

        message = b''
        while not message_complete:
            part = conn.recv(buffer_length)
            message += part

            if len(part) < buffer_length:
                break

        message = message.decode('utf8')
        print('{} Echoed: {}'.format(
            datetime.now().strftime('%H:%M:%S %d-%m-%y'), message))

        conn.sendall(message.encode('utf8'))

    except KeyboardInterrupt:
        try:
            conn.close()
        except NameError:
            pass

        sock.close()
        print('--- Stopping server on port {} at {} ---'.format(
            PORT, datetime.now().strftime('%H:%M:%S %d-%m-%y')))

    conn.close()
    sock.close()
    print('--- Stopping server on port {} at {} ---'.format(
        PORT, datetime.now().strftime('%H:%M:%S %d-%m-%y')))


if __name__ == '__main__':
    start_server()
