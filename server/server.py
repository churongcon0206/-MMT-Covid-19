import socket

HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf8"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST, SERVER_PORT))
s.listen()

print("SERVER SIDE")
print("Server: ", HOST, SERVER_PORT)
print("Waitting for Client")

connection, addr = s.accept()

print("Client address: ", addr)
print("connection:", connection.getsockname())

username = connection.recv(1024).decode(FORMAT)
connection.sendall(username.encode(FORMAT))

print("username", username)
passwork = connection.recv(1024).decode(FORMAT)
print("passwork:", passwork)

input()