"""Interactive TCP/IP terminal"""
import tcp
import download
import upload


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

        while True:
            command = input("> ")
            # Process commands
            if command.lower() == "exit":
                break
            elif command.lower() == "download":
                download.download(sock)
            elif command.lower() == "upload":
                upload.upload(sock)
            else:
                tcp.send(sock, command)
                data = tcp.receive(sock)
                print(data)

    finally:
        sock.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()
