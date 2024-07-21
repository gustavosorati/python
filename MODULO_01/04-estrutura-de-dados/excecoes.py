# Eventos que ocorrem durante a execução do código, impedindo 
# o funcionamento correto do software

print("Exemplo de captura de exceções")

while True:
    try:
        numero = int(input("Digite um número inteiro:"))
        resultado = 10 / numero

    except ValueError as e:
        print(f"Erro de value error: {e}")
        raise ValueError("Tipo de variáveis incompatíveis")
    except Exception as error:
        print(f"Erro: {error}")
    else: 
        print(resultado)
        break
    finally:
        print("Operação finalizada")

