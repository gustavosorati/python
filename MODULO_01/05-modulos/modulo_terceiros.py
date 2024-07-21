""" Iremos utilizar o pacote request
    Precisamos abrir o terminal e instalar ele antes de podermos fazer o import
    pip install requests==2.31.0
"""

print("\nImportação e uiso de módulos de terceiros")
import requests 

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação HTTP para {url} retornou o status {response.status_code}")