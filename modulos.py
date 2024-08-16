#modulos padrões do python	

from math import sqrt
# import math : importa todas as funcões de math

raiz = sqrt(25)

print(raiz) 

print("\nExemplo de criação e ultilização de um módulo personalizado\n")

import meu_modulo

mensagem = meu_modulo.saudacao("Marcos")
print(mensagem)

numero = meu_modulo.dobro(5)
print(numero)