#Importaçao de modulos de terceiros	

print("\nExemplo de criação e ultilização de um módulo de terceiros\n")
import requests

response = requests.get("https://www.google.com")
print(response.status_code)