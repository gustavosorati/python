# Loop estrutura que permite executar uma tarefa até que sua condição se torne false

# For lista
lista = [9, 2, 3, 4, 5]
print("for utilizando lista")
for elemento in lista:
    print("Elemento", elemento)

tupla = (1, 2, 3, 4, 5)
print("\nfor utilizando tupla")
for elemento in tupla:
    print("Elemento", elemento)

pessoa = {"nome": "Gustavo", "idade": 29, "cidade": "Orlândia"}
print("\nfor utilizando dicionário - chave")
for chave in pessoa.keys():
    print(chave)

print("\nfor utilizando dicionário - valores")
for value in pessoa.values():
    print(value)

print("\nfor utilizando dicionário - valores")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# range(): intervalo númerico em formato de lista
print("\nfor utilizando a função range()")
for index in range(0, 10):
    print("Número:", index)

print("\nfor utilizando a função range() + len()")
for index in range(0, len(lista)):
    print("Número:", lista[index])

print("\nfor utilizando a função enumerate()")
for chave, valor in enumerate(lista):
    print(f"{chave}: {valor}")
