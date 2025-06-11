from xmlrpc.server import SimpleXMLRPCServer

def cuadrado(n):
    return n * n

server = SimpleXMLRPCServer(("localhost", 8000))
print("[RPC Servidor] Esperando llamadas en el puerto 8000...")
server.register_function(cuadrado, "cuadrado")
server.serve_forever()
