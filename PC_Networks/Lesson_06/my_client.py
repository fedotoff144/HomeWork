import socket
import threading

nickname = input('Enter your name please: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def recive():
    while True:
        try:
            massage = client.recv(1024).decode('ascii')
            if massage == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(massage)
        except:
            print('Some error!')
            client.close
            break

def write():
    while True:
        massage = '{}: {}'.format(nickname, input(''))
        client.send(massage.encode('ascii'))

recive_thread = threading.Thread(target=recive)
recive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


# netstat -n        - in Windows terminal
# ss -tulpan        - in Linux termial for watching chat