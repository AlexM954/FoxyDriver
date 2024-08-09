"""RAW TCP connection functions"""
import socket
import queue


def init_queue():
    return queue.Queue()


def connect(ip, port, timeout=1):
    try:
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        sock.settimeout(timeout)
        sock.connect((ip, port))
        print(f"Connected to {ip} on port {port}")

        return sock

    except Exception as e:
        print(f"Failed to connect to {ip} on port {port}: {e}")
        return None


def send(sock, data):
    try:
        # Commands require \r to be processed properly.
        enc_data = (data + '\r').encode()
        sock.sendall(enc_data)

    except Exception as e:
        print(f"Failed to send data: {e}")


def receive(sock, queue, buffer_size=4096, alive=[True]):
    while alive[0]:
        try:
            response = sock.recv(buffer_size)
            if response:
                queue.put(response)

        except TimeoutError:
            pass
