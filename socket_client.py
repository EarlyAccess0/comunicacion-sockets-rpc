import socket

HOST = 'localhost'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    mensaje = input("Ingrese un mensaje para el servidor: ")
    s.sendall(mensaje.encode())
    data = s.recv(1024).decode()
    print(f"[Cliente] Respuesta del servidor: {data}")
