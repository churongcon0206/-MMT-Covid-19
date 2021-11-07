import socket

HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("CLIENT SIDE")
client.connect((HOST, SERVER_PORT))
print("Client address:", client.getsockname())

username = input("username: ")
passwork = input("passwork: ")
client.sendall(username.encode(FORMAT))
client.recv(1024).decode(FORMAT)
client.sendall(passwork.encode(FORMAT))
input()