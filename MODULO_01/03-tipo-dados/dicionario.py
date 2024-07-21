# Coleção não ordenada de pares chave e valor

pessoa = {"nome": "Gustavo", "idade": 29, "cidade": "Orlândia"}

print("Meu dicionário:", pessoa)
print("Meu dicionário, nome:", pessoa["nome"])

pessoa["sobrenome"] = "Sorati"
print("Sobrenome:", pessoa["sobrenome"])


# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário:", pessoa)

# Métodos: Keys(), values(), items()
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

valores = list(pessoa.values())
print("Chaves do dicionário:", valores)
print("Chaves do dicionário:", valores[0])

# Métodos itens
itens = list(pessoa.items())
print("Pares chave-valor do dicionário: ", itens)
print("Primeiro valor: ", itens[0][1])

