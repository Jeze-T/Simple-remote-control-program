import socket
import os

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = '192.168.xxx.xxx'  #服务端的ip地址
    port = 5555
    s.connect((host,port))

    while True:
        data_recv = s.recv(1024).decode("utf-8") #先接收，看别人发啥(欢迎连接~)
        print(data_recv)
        msg = input("send msg:")
        s.send(msg.encode("utf-8"))

    s.close()

    pass


if __name__ == '__main__':
    main()

    #pyinstaller，生成exe文件

