from typing import List, Dict

# Programa para gerenciar contatos

contatos: List[Dict[str, str | bool]] = []

def criarContato(lista: List[Dict[str, str | bool]], nome: str, telefone: str, email: str) -> None:
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    lista.append(contato)

    print(f"\nContato cadastrado com sucesso.\n")
    return

def ver_contatos(lista: List[Dict[str, str | bool]]) -> None:
    if len(lista) == 0:
        print("\nVocê não possui nenhum contato.\n")
    else:
        print("\nLista de contatos:")
        for indice, contato in enumerate(lista):
            status = "X" if contato["favorito"] else " "
            nome_contato = contato["nome"]
            email = contato["email"]
            telefone = contato["telefone"]
            print(f"{indice}. [{status}] {nome_contato} - {email} - {telefone}")
            print() 
    return

def atualizar_contato(contatos: List[Dict[str, str | bool]], indice_contato: int, nome: str, email: str, telefone: str) -> None:
    if len(contatos) == 0:
        print("\nVocê não possui nenhum contato.\n")
        return

    if 0 <= indice_contato < len(contatos):
        if len(nome) > 0:
            contatos[indice_contato]["nome"] = nome
        
        if len(email) > 0:
            contatos[indice_contato]["email"] = email

        if len(telefone) > 0:
            contatos[indice_contato]["telefone"] = telefone

        print(f"\nContato {indice_contato} atualizado com sucesso.\n")
    else:
        print("\nÍndice de tarefa inválido.\n")
    return

def favoritar_contato(contatos: List[Dict[str, str | bool]], indice_contato: int) -> None:
    if len(contatos) == 0:
        print("\nVocê não possui nenhum contato.\n")
        return

    if 0 <= indice_contato < len(contatos):
        contatos[indice_contato]["favorito"] = True

        print(f"\nContato {contatos[indice_contato]['nome']} marcado como favorito.\n")
    else:
        print("\nÍndice de tarefa inválido.\n")
    return

def deletar_contato(contatos: List[Dict[str, str | bool]], indice_contato: int):
    if len(contatos) == 0:
        print("\nVocê não possui nenhum contato.\n")
        return

    if 0 <= indice_contato < len(contatos):
        del contatos[indice_contato]
        print("\nContato deletado com sucesso.\n")
    else:
        print("\nÍndice de contato inválido.\n")
    return

def validar_indice(mensagem: str, limite: int) -> int:
    while True:
        try:
            indice = int(input(mensagem))
            if 0 <= indice < limite:
                return indice
            else:
                print("\nÍndice inválido. Tente novamente.\n")
        except ValueError:
            print("\nEntrada inválida. Digite um número.\n")

while True:
    print("\n---------------- Contact.py ----------------")
    print("1. Criar contato")
    print("2. Ver contatos")
    print("3. Atualizar contato")
    print("4. Favoritar contato")
    print("5. Deletar contatos")
    print("6. Sair")
    print("--------------------------------------------------------------------------")

    escolha = input("O que deseja fazer? ")

    if escolha == "1":
        contato = input("Informe o nome: ")
        telefone = input("Informe o telefone: ")
        email = input("Informe o email: ")
        criarContato(contatos, contato, telefone, email)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)

        if contatos:
            indice_contato = validar_indice("Digite o índice do contato que deseja atualizar: ", len(contatos))
            novo_nome = input("Digite o novo nome do contato: ")
            novo_email = input("Digite o novo email do contato: ")
            novo_telefone = input("Digite o novo telefone do contato: ")

            atualizar_contato(contatos, indice_contato, novo_nome, novo_email, novo_telefone)
    elif escolha == "4":
        ver_contatos(contatos)

        if contatos:
            indice_contato = validar_indice("Qual contato deseja favoritar?: ", len(contatos))
            favoritar_contato(contatos, indice_contato)

    elif escolha == "5":
        ver_contatos(contatos)

        if contatos:
            indice_contato = validar_indice("Qual contato deseja deletar?: ", len(contatos))
            deletar_contato(contatos, indice_contato)

    elif escolha == "6":
        break







