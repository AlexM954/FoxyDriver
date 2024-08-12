"""Download a program from a Foxy R1 fraction collector"""
import os
import time
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


def download(sock, queue):
    num = input("Enter number of program to download (1-8): ")
    for cmd in ["Remote", "Program=" + num]:
        tcp.send(sock, cmd)
        time.sleep(0.1)

    for cmd in command_list:
        tcp.send(sock, cmd)
        time.sleep(0.1)

    path = os.path.abspath(os.getcwd())
    filename = path + "\\programs\\program_" + num + ".txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as txt:
        while not queue.empty():
            txt.write(queue.get().rstrip().decode() + '\n')

    print("\nProgram downloaded succesfully.")
