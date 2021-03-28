  
import os 

os.system('cls')

print("****************************************************************")
print("* ╔╦╗╦═╗  ╔═╗╦═╗╔═╗═╗ ╦╦ ╦  ╦╔═╗  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗        *")
print("* ║║║╠╦╝  ╠═╝╠╦╝║ ║╔╩╦╝╚╦╝  ║╠═╝  ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝        *")
print("* ╩ ╩╩╚═  ╩  ╩╚═╚═╝╩ ╚═ ╩   ╩╩    ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═        *")
print("* Copyright of Mr.Proxy, 2021                                  *")
print("* Tipe X if you want to LEAVE!                                 *")
print("* https://github.com/Mr-Proxy-source                           *")
print("* https://www.youtube.com/c/MrProxy1                           *")
print("****************************************************************")

while True:
    ip = input("Type IP for Ping: ")

    if ip == 'x':
        print('You are leaving')
        break

print('-' * 55)
os.system('ping {}'.format(ip))
print('-' * 55)
