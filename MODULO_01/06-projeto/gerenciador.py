from typing import List, Dict

# Programa para gerenciar tarefas

tarefas: List[Dict[str, bool]] = []

def criar_tarefa(lista: List[Dict[str, bool]], nome_tarefa: str) -> None:
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    lista.append(tarefa)
    print(f"\nTarefa '{nome_tarefa}' foi adicionada com sucesso.\n")
    return

def ver_tarefas(lista: List[Dict[str, bool]]) -> None:
    if len(lista) == 0:
        print("\nNão há nenhuma tarefa.\n")
    else:
        print("\nLista de Tarefas:")
        for indice, tarefa in enumerate(lista):
            status = "X" if tarefa["completada"] else " "
            nome_tarefa = tarefa["tarefa"]
            print(f"{indice}. [{status}] {nome_tarefa}")
        print() 

def atualizar_nome_tarefa(tarefas: List[Dict[str, bool]], indice_tarefa: int, novo_nome_tarefa: str) -> None:
    if len(tarefas) == 0:
        print("\nNão há nenhuma tarefa.\n")
        return

    if 0 <= indice_tarefa < len(tarefas):
        tarefas[indice_tarefa]["tarefa"] = novo_nome_tarefa
        print(f"\nTarefa {indice_tarefa} atualizada para '{novo_nome_tarefa}'.\n")
    else:
        print("\nÍndice de tarefa inválido.\n")
    return

def completar_tarefa(tarefas: List[Dict[str, bool]], indice_tarefa: int) -> None:
    if len(tarefas) == 0:
        print("\nNão há nenhuma tarefa.\n")
        return

    if 0 <= indice_tarefa < len(tarefas):
        tarefas[indice_tarefa]["completada"] = True
        print(f"\nTarefa {indice_tarefa} marcada como completada.\n")
    else:
        print("\nÍndice de tarefa inválido.\n")
    return

def deletar_tarefas_completadas(tarefas: List[Dict[str, bool]]):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)

    print("Tarefas completadas foram deletadas.")
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
    print("\n---------------- Menu do Gerenciador de Lista de Tarefas ----------------")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")
    print("--------------------------------------------------------------------------")

    escolha = input("O que deseja fazer? ")

    if escolha == "1":
        nome_tarefa = input("Informe o nome da tarefa: ")
        criar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        if tarefas:
            indice_tarefa = validar_indice("Digite o índice da tarefa que deseja atualizar: ", len(tarefas))
            novo_nome = input("Digite o novo nome da tarefa: ")
            atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == "4":
        ver_tarefas(tarefas)
        if tarefas:
            indice_tarefa = validar_indice("Qual tarefa deseja completar: ", len(tarefas))
            completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
    elif escolha == "6":
        break







