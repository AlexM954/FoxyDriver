"""Interactive TCP/IP terminal"""
import threading
import time
from . import tcp


def main():

    ip = input("Enter ip address: ")
    port = int(input("Enter port: "))

    sock = tcp.connect(ip, port, 1)
    if sock is None:
        return

    try:
        print("Enter command to send.")
        print("    or Exit to quit.")
        print("    or Download to download a program.")
        print("    or Upload to download a program.")

        # Set up response queue and threads.
        queue = tcp.init_queue()
        thread_stop = threading.Event()

        thread_stop.set()

        recv_thread = threading.Thread(
            target=tcp.receive,
            args=(sock, queue, thread_stop, 4096)
        )

        proc_thread = threading.Thread(
            target=tcp.process,
            args=(sock, queue, thread_stop)
        )

        recv_thread.start()
        proc_thread.start()

        while True:
            command = input("> ")
            # Process commands
            if command.lower() == "exit":
                queue.put(None)
                thread_stop.clear()
                break
            elif command.lower() == "download":
                queue.put(b"download")
            elif command.lower() == "upload":
                queue.put(b"upload")
            else:
                tcp.send(sock, command)
                time.sleep(0.1)

    finally:
        # Clean up.
        print("Closing connection.")
        time.sleep(2.5)
        sock.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()
