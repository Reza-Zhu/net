import socket
import threading
import time
host = socket.gethostname()
def send():
    s = socket.socket()
    port1 = 12345
    s.bind((host, port1))
    s.listen(5)
    c, addr = s.accept()
    print('连接地址：', addr)
    while True:
        t = input('请输入要发送的消息:\n ')
        t = '你收到了来自(端口)的消息：'+ t
        c.send(t.encode('utf-8'))

def get():
    a = socket.socket()
    port2 = 9999
    time.sleep(10)
    try:
        a.connect((host, port2))
        while True:
            print(a.recv(1024).decode('utf-8'))
    except:print("错误：请求连接超时......请在10s内打开get.py程序建立连接")
def main():
    t1=threading.Thread(target=send)
    t2=threading.Thread(target=get)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()

