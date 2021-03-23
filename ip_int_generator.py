print("*****************************************************************")
print("* ╔╦╗╦═╗  ╔═╗╦═╗╔═╗═╗ ╦╦ ╦  ╦╔═╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗   *")
print("* ║║║╠╦╝  ╠═╝╠╦╝║ ║╔╩╦╝╚╦╝  ║╠═╝  ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝   *")
print("* ╩ ╩╩╚═  ╩  ╩╚═╚═╝╩ ╚═ ╩   ╩╩    ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═   *")
print("* Copyright of Mr.Proxy, 2021                                   *")
print("* https://github.com/Mr-Proxy-source                            *")
print("* https://www.youtube.com/c/MrProxy1                            *")
print("*****************************************************************")

ip = input("Enter IP for further processing: ")
delovi = ip.split(".")
print("#" * 55)

print(type(delovi))
print(delovi)

print("#" * 55)
donji_ip = int(input("Lower IP: "))
gornji_ip = int(input("Upper IP: "))
print("#" * 55)

#print(ip, donji_ip, gornji_ip)

Lista = open('ip_list.txt', 'w')

print("#" * 55)
for x in range(donji_ip, gornji_ip):
    print(delovi[0] + "." + delovi[1] + "." + delovi[2] + "." + str(x))
    Lista.write((delovi[0] + "." + delovi[1] + "." + delovi[2] + "." + str(x) + "\n"))
print("#" * 55)

Lista.close()
