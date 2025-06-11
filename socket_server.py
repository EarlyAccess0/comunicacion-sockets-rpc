import socket

HOST = 'localhost'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[Servidor] Esperando conexión en {HOST}:{PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"[Servidor] Conectado por {addr}")
        data = conn.recv(1024).decode()
        print(f"[Servidor] Mensaje recibido: {data}")
        conn.sendall("Mensaje recibido correctamente.".encode())
