import socket
import os

os.system('cls')


print("*****************************************************************")
print("* ╔╦╗╦═╗  ╔═╗╦═╗╔═╗═╗ ╦╦ ╦                                      *")
print("* ║║║╠╦╝  ╠═╝╠╦╝║ ║╔╩╦╝╚╦╝                                      *")
print("* ╩ ╩╩╚═  ╩  ╩╚═╚═╝╩ ╚═ ╩                                       *")
print("* Copyright of Mr.Proxy, 2021                                   *")
print("* https://github.com/Mr-Proxy-source                            *")
print("* https://www.youtube.com/c/MrProxy1                            *")
print("*****************************************************************")

while True:
    site = input('Tipe hostname of site you want resolve: ')
    print("****************************************************************")

    print(socket.gethostbyname(site))

    print('-' * 55)
