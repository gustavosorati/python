nome_completo = "Gustavo Sorati"
nome_completo_aspas = """Gustavo
Sorati"""

nome_completo_quebra = "Gustavo \
Sorati"

nome = "Gustavo"
sobrenome = "Sorati"

print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma): " + nome_completo)
print("Nome completo (3a forma): " + "Gustavo" + " Sorati")
print("Nome completo (4a forma): " + "Gustavo", "Sorati")
print("Nome completo (5a forma): " + nome_completo_aspas)
print("Nome completo (6a forma): " + nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome)) # faz transformação e + segura
print(f"Nome completo (9a forma): {nome} {sobrenome}") # + visualmente agradável
print("Nome completo (10a forma): {} {}".format(nome, sobrenome))
