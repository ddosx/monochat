#Client-side code
import socket, threading
print ("""
█████████████████████████████████████████████████
█▄─▀█▀─▄█─▄▄─█▄─▀█▄─▄█─▄▄─█─▄▄▄─█─█─██▀▄─██─▄─▄─█
dexdex monochat uniclient beta█▀█─▄─██─▀─████─███
▀▄▄▄▀▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▀▄▄▀▀▄▄▄▀▀""")
nickname = input("Выберите никнейм: ")
print("Подключаемся к серверу...")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     
client.connect(('192.168.31.56', 6677))#вот тут меняй айпи и порт
print("Подключились!")
def receive():
    while True:                                                 
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except: #вот тут пиши айпишники серверов
            print("""Что-то пошло не так.
                Возможно, у вас неправильно задан IP и порт сервера.
                Откройте файл monochat.py в редакторе и измените IP на IP сервера, к которому вы хотите подключиться:
                
                Сервер      IP              Порт
                Main        192.168.31.56   6677""")
            client.close()
            break
def write():
    while True:                                                
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)               
receive_thread.start()
write_thread = threading.Thread(target=write)                  
write_thread.start()