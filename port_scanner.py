
import socket, os

os.system('cls')

###In this field where is tipe 'HERE YOUR IPV4 ADDRESS' tipe in there you IPV4 address ***DONT DELETE '' IF YOU DELETE IT SCRIPT WILL NOT DOING***

print("*****************************************************************")
print("* ╔╦╗╦═╗  ╔═╗╦═╗╔═╗═╗ ╦╦ ╦                                      *")
print("* ║║║╠╦╝  ╠═╝╠╦╝║ ║╔╩╦╝╚╦╝                                      *")
print("* ╩ ╩╩╚═  ╩  ╩╚═╚═╝╩ ╚═ ╩                                       *")
print("* Copyright of Mr.Proxy, 2021                                   *")
print("* https://github.com/Mr-Proxy-source                            *")
print("* https://www.youtube.com/c/MrProxy1                            *")
print("*****************************************************************")


ip = '89.216.217.225'
port_list = [20, 80, 8080, 139, 445, 23, 21, 22]

for x in port_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection = s.connect_ex((ip, x))

    if connection == 0:
        print("#" * 55)
        print("Port: ", x, 'is OPENED')
        print("#" * 55)
    else:
        print("Port: ", x, 'is CLOSED')
