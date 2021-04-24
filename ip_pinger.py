  
import os 
import ip_pinger

os.system('cls')

print("""
___  ___      ______                      _____      
|  \/  |      | ___ \                    |_   _|     
| .  . |_ __  | |_/ / __ _____  ___   _    | | _ __  
| |\/| | '__| |  __/ '__/ _ \ \/ / | | |   | || '_ \ 
| |  | | |    | |  | | | (_) >  <| |_| |  _| || |_) |
\_|  |_/_|    \_|  |_|  \___/_/\_\\__, |  \___/ .__/ 
                                   __/ |      | |    
                                  |___/       |_|    
 _____ _               _             
/  __ \ |             | |            
| /  \/ |__   ___  ___| | _____ _ __ 
| |   | '_ \ / _ \/ __| |/ / _ \ '__|
| \__/\ | | |  __/ (__|   <  __/ |   
 \____/_| |_|\___|\___|_|\_\___|_|   """)
    

    
print("****************************************************************")
print("* Copyright of Mr.Proxy, 2021                                  *")
print("* https://github.com/Mr-Proxy-source                           *")
print("* https://www.youtube.com/c/MrProxy1                           *")
print("****************************************************************")

ip_to_check = input('Tipe IP for Ping: ')

print('-' * 60)
os.system('ping {}'.format(ip_to_check))
print('-' * 60)

input('Press Enter to Ping again')
