
import socket

socket_severs = socket.socket() # : socket.socket

socket_severs.bind(("localhost",8888))


socket_severs.listen(1)


conn,address = socket_severs.accept()

print(f"连接成功,信息{address}")

while True:
    data = conn.recv(1024).decode("utf-8")
    print(f"收到信息：{data}")
    msg = input("输入回复信息以回车结束")
    if msg == "exit" :
        break

    conn.send(msg.encode("utf-8"))

conn.close()
socket_severs.close ()