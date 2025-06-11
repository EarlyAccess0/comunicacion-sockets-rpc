import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
numero = int(input("Ingrese un número para calcular su cuadrado: "))
resultado = proxy.cuadrado(numero)
print(f"El cuadrado de {numero} es {resultado}")
