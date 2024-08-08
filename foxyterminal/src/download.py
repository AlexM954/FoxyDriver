"""Download a program from a Foxy R1 fraction collector"""
import os
from . import tcp


command_list = [
    "Program",
    "Delay",
    "Fsize",
    "Ftype",
    "Last",
    "Nonpeak",
    "Pattern",
    "Range",
    "Restart",
    "Rstime",
    "Rtype",
    "Threshold",
    "Width",
    "Window=1",
    "Window",
    "Wend",
    "Wstart",
    "Window=2",
    "Window",
    "Wend",
    "Wstart",
    "Window=3",
    "Window",
    "Wend",
    "Wstart",
    "Window=4",
    "Window",
    "Wend",
    "Wstart",
]


def download(sock):
    tcp.send(sock, "Remote")
    num = input("Enter number of program to download (1-8): ")
    tcp.send(sock, "Program=" + num)

    prog = []

    for cmd in command_list:
        tcp.send(sock, cmd)
        data = tcp.receive(sock)
        if data:
            prog.append(data)
        else:
            prog.append("")

    path = os.path.abspath(os.cwd())
    filename = path + "\\programs\\program_" + num + ".txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as txt:
        for line in prog:
            txt.write(line.rstrip() + '\n')

    print("Program downloaded succesfully.")
