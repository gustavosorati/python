# Bloco ou instruções que podem ser utilizados por outros arquivos
# Módulo padrão - já vme com o python

print("Exemplo de importação de um módulo padrão:")
# import math
from math import sqrt

# raiz_quadrada = math.sqrt(25)
raiz_quadrada = sqrt(25)
print(raiz_quadrada)

print("\n Exemplo de criação de módulo personalizado")
import meu_modulo

print(meu_modulo.saudacao("Gustavo"))
print(meu_modulo.dobro(4))

