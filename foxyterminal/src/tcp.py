"""RAW TCP connection functions"""
import socket


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


def receive(sock, buffer_size=4096):
    try:
        data = sock.recv(buffer_size).decode()
        return data

    except Exception:
        return None
