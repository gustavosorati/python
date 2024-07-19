# Coleção ordenada e imutável de elementos
minha_tupla = (1, 2, 3, 4)

print("Minha tupla:", minha_tupla)

print("Minha tupla[0]:", minha_tupla[0])
print("Minha tupla[2]:", minha_tupla[2])
print("Minha tupla[-1]:", minha_tupla[-1])

# método count
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

indice = minha_tupla.index(3)
print("Índice do elemento 3:", indice)
