import socket
from subprocess import Popen, DEVNULL
import tkinter as tk

#host = 'localhost'

porta = 50000
ipa = "192.168.1.217"
ip = ["192.168.1.200", "192.168.2.200", "192.168.3.200", "192.168.4.200", "192.168.5.200", "192.168.6.200", "192.168.7.200", "192.168.8.200", "192.168.9.200", "192.168.10.200", "192.168.11.200", "192.168.12.200", "192.168.13.200", "192.168.14.200", "192.168.15.200", "192.168.16.200", "192.168.17.200", "192.168.18.200", "192.168.19.200", "192.168.20.200", "192.168.21.200", "192.168.22.200", "192.168.23.200", "192.168.24.200", "192.168.25.200", "192.168.26.200", "192.168.27.200", "192.168.28.200", "192.168.29.200", "192.168.30.200", "192.168.31.200", "192.168.32.200", "192.168.33.200", "192.168.34.200"]



def verificar():
    #for i in ip:
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serv.bind((ipa, porta))
        resultado = serv.connect_ex((ipa, porta))
        serv.close()

        if resultado == 0:
            print(True)
        else:
            print(False)




verificar()