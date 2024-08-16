# comentario uma linha

""" comentario
    varias
    linhas
"""

#SnakeCase
nome_completo = "Marcos Maio"

#CamelCase

nomeCompleto = "Marcos Maio"

#Inteiro
numero_inteiro = 5
print("numero inteiro", numero_inteiro)

#Float
numero_float = 2.5
print("numero float", numero_float)

#type
print("type", type(numero_inteiro))

#soma
soma = numero_inteiro + numero_float
print("soma", soma)

#subtração
subtracao = numero_inteiro - numero_float
print("subtração", subtracao)

#multiplicação
multiplicacao = numero_inteiro * numero_float
print("multiplicação", multiplicacao)

#divisão
divisao = numero_inteiro / numero_float
print("divisão", divisao , type(divisao))

#modulo
modulo = numero_inteiro % numero_float
print("modulo", modulo)

#divisão inteira
divisao_inteira = numero_inteiro // numero_float
print("divisão inteira", divisao_inteira)

#conversão
print (int(divisao))

idade = 25

if idade < 18:
  print("menor de idade")  
else:
  print("maior de idade")
  
#Formatação de string
print ("Nome:", nome_completo)
print ("Nome:" + nome_completo)
print ("Nome:" + nome_completo + "Idade:" + str(idade))
print ("Nome: " + "Marocos " + "Idade: " + str(idade))
print ("Nome: %s " % nome_completo)
print ("Nome: %s Idade: %s" % (nome_completo, idade))
print (f"Nome: {nome_completo} Idade: {idade}")

#Métodos

print (nome_completo.upper())
print (nome_completo.lower())
print (nome_completo.capitalize())
print (nome_completo.title())

print (nome_completo.find("s"))
print (nome_completo.count("a"))
print (nome_completo.replace("a", "123"))
print("-".join(nome_completo))
print (nome_completo.split(" "))
print(nome_completo.encode())
print(nome_completo.encode().decode())

nome_completo = "XMarcos MaioX"
print(nome_completo.strip("X"))
print(nome_completo.startswith("XMa"))
print(nome_completo.startswith("M"))

print ("Marcos" in nome_completo)
print ("abc" not in nome_completo)

idade = 25
nome = "Marcos"

# Usando 'and'
if idade > 18 and nome == "Marcos":
    print("Maior de idade e nome é Marcos")

# Usando 'or'
if idade > 18 or nome == "Marcos":
    print("Maior de idade ou nome é Marcos")

#lista e manipulações

lista = [1, 2, 3, 4, 5, "Marcos", 2.5, True, False]

print(lista[0])
print(lista[1:8])
print(lista[:6])

lista[0] = 10
print(lista)

lista.append(6)
print(lista)

indice = lista.index("Marcos")
print(indice)

lista.insert(1, 20)
print(lista)

lista.pop(4) #indice -1 = 4
print(lista) 

lista.remove("Marcos")
print(lista) 

lista_2 = [120, 201, 30, 4, 15, 2.5, 678, 90 , 10]

lista_2.sort()

print(lista_2)

#tupla
lista_tupla = (1, 2, 3, 4, 5, "Marcos", 2.5, True, False) #não pode ser alterada

#dicionario
pessoa = {"nome": "Marcos", "idade": 22, "cidade": "Rio de Janeiro"}
print(pessoa)

print(pessoa["nome"])
print(pessoa["idade"]) 
print(pessoa["cidade"])

pessoa["sobrenome"] = "Maio" 
print(pessoa)

del pessoa["sobrenome"]

print(pessoa)

#indices
print(pessoa.keys())

#caso necessite de uma lista de chaves ou valores deve-se converter para lista primeiro
keys = list(pessoa.keys())
print(keys[0])

#valores

print(pessoa.values())

#transformar dicionario em tupla 
items = list(pessoa.items())
print(items)

#condicionais

# idade = int(input("Digite sua idade: "))

if idade >= 18:
  print("Maior de idade")
elif idade >= 12:
  print("Adolescente")
else:
  print("Criança")
  
#Ternário
mensagem = "VocÊ pode tirar carteira de habilitação" if idade >= 18 else "Você não pode tirar carteira de habilitação"

print(mensagem)

#loops

lista = [1,2,3,4,5]

for items in lista:
  print(items)
  
pessoa = {"nome": "Marcos Maio", "idade": 22, "cidade": "Rio De Janeiro"}

for chave, valor in pessoa.items():
  print(f"{chave}: {valor}")
  
print(list(range(0,10)))

# for nums in range(6):
#   print(nums)
print(lista)
for i in range(len(lista)):
  print("Indice:", i)
  print("Elemento:", lista[i])
  if i == 3:
    lista[i] = 6
  else:
    lista[i] = "e isso ai" #ou um número neh

print(lista)

#while

count = 0

while count <= 10:
  print("Contagem:", count)
  count += 1
  
  if count == 5:
    print("metade huwuuuuu")
    
    
#função

def quadrado(num):
  result = num ** 2
  return result 

print("Chamando função passando 2:", quadrado(2))

#exceções

try:
  numero = int(input("Digite um número: ")) #se digitar uma letra vai dar erro
  resultado = 10 / numero
except ValueError as e:
  print("Erro:", e) #mensagem de erro
except Exception as e:
  print("Erro:", e) #mensagem de erro
else: #se não der erro
  print(f"Resultado: {resultado}")
finally: #sempre vai ser executado mesmo se der certo ou errado
  print("Fim do programa")