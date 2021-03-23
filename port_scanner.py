import socket, os

os.system('cls')


print("*****************************************************************")
print("* ╔╦╗╦═╗  ╔═╗╦═╗╔═╗═╗ ╦╦ ╦                                      *")
print("* ║║║╠╦╝  ╠═╝╠╦╝║ ║╔╩╦╝╚╦╝                                      *")
print("* ╩ ╩╩╚═  ╩  ╩╚═╚═╝╩ ╚═ ╩                                       *")
print("* Copyright of Mr.Proxy, 2021                                   *")
print("* https://github.com/Mr-Proxy-source                            *")
print("* https://www.youtube.com/c/MrProxy1                            *")
print("*****************************************************************")


ip = 'HERE YOUR IPV4 IP ADDRES'
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
