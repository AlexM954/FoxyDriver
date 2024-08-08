"""Upload a program to a Foxy R1 fraction collector"""
import os
import time
from . import tcp


def upload(sock):
    tcp.send(sock, "Remote")
    file = input("Enter filename of program to upload: ")

    path = os.path.abspath(os.cwd())

    with open(path + "\\programs\\" + file, 'rb') as program:
        for line in program:
            command = line.rstrip() + b'\r'
            tcp.send(sock, command)
            time.sleep(0.5)

    print("Program uploaded succesfully.")
