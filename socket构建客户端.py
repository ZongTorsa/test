
import socket

socket_client = socket.socket() # : socket.socket

socket_client.connect(("localhost",8888))

socket_client.send("hello".encode("utf-8"))

recv_data = socket_client.recv(1024)
print(f"收到的信息是{recv_data.decode('utf-8')}")


socket_client.close()