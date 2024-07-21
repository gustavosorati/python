# listas

minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

print("minha_lista[0]", minha_lista[0])
print("minha_lista[1:3]", minha_lista[1:3])
print("minha_lista[:5]", minha_lista[:6])
print("minha_lista[2:]", minha_lista[2:])

minha_lista.append(6)
print("Após append(6):", minha_lista)

indice = minha_lista.index(6)
print("Índice do elemento 6:", indice)

minha_lista.insert(3, 999)
print("Após o insert:", minha_lista)

minha_lista.pop(4)
print("Após o pop:", minha_lista)

minha_lista.remove(True)
print("Após o remove(True):", minha_lista)

# o sort não irá funcionar pois a lista elementos de tipos diferentes.
minha_lista.sort()
print("Após o sort:", minha_lista)