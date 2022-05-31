#Server-side code 

import socket, threading                                                
print ("""

█▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀ █  █ █▀▀█ ▀▀█▀▀ 
dexdex monochat server code beta▄█   █   
▀   ▀ ▀▀▀▀ ▀  ▀ ▀▀▀▀ ▀▀▀ ▀  ▀ ▀  ▀   ▀   

Setting ip and port of the server...""")
host = '192.168.31.56' #пиши ip a и ставь сюда тот, у которого меньше последние цифры.                                                  
port = 6677                                                             
print ("Done. Opening socket...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              
server.bind((host, port))                                               
print("Socket is opened on",host,"port",port,". Listening.")
server.listen()

clients = []
nicknames = []

def broadcast(message):                                                 
    for client in clients:
        client.send(message)

def handle(client):                                         
    while True:
        try:                                                            
            message = client.recv(1024)
            broadcast(message)
        except:                                                         
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():                                                          
    while True:
        client, address = server.accept()
        print("v This users ip adress: {}".format(str(address)))       
        client.send('NICKNAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print("User {} joined".format(nickname))
        broadcast("{} connected!".format(nickname).encode('ascii'))
        client.send('You are connected to the Main server. Pozhaluista, ne pishi na russkom, krashnet klient'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()