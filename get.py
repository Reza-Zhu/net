import socket
import threading
import time
host = socket.gethostname()
def send():
    s = socket.socket()
    port1 = 9999
    s.bind((host, port1))
    s.listen(5)
    c, addr = s.accept()
    print('连接地址：', addr)
    o='****连接建立成功****'
    c.send(o.encode('utf-8'))
    while True:
        t = input('请输入要发送的消息:\n ')
        t = '你收到了来自(端口)的消息：' + t
        c.send(t.encode('utf-8'))

def get():
    a = socket.socket()
    port2 = 12345
    a.connect((host, port2))
    while True:
        print(a.recv(1024).decode('utf-8'))
def main():
    time.sleep(5)
    t2 = threading.Thread(target=get)
    t1 = threading.Thread(target=send)
    t2.start()
    t1.start()

if __name__ == '__main__':
    main()

