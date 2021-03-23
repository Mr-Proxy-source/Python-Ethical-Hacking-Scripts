######################################
#Copyright of Mr.Proxy, 2021         #
#https://github.com/Mr-Proxy-source  #
#https://www.youtube.com/c/MrProxy1  #
######################################

import socket, os


while True:
    print("*****************************************************************")
    print("* ╔╦╗╦═╗  ╔═╗╦═╗╔═╗═╗ ╦╦ ╦                                      *")
    print("* ║║║╠╦╝  ╠═╝╠╦╝║ ║╔╩╦╝╚╦╝                                      *")
    print("* ╩ ╩╩╚═  ╩  ╩╚═╚═╝╩ ╚═ ╩                                       *")
    print("* Copyright of Mr.Proxy, 2021                                   *")
    print("* https://github.com/Mr-Proxy-source                            *")
    print("* https://www.youtube.com/c/MrProxy1                            *")
    print("*****************************************************************")
    site = input('Tipe hostname of site you want resolve: ')
    print("****************************************************************")
    print(socket.gethostbyname(site))
    print('-' * 55)
