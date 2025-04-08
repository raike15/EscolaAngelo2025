 # DICIONÁRIO X CONJUNDO X LISTA X TUPLA

n1 = 9
n2 = 7
n3 = 13

numeros = [9,7,13]
numeros.append(21)
numeros.remove(9)
print(numeros[0])

numeros = (9,7,13) # é uma tupla
#não tem como adicionar,remover
print(numeros[0])

conjunto = set()
conjunto.add(9)
conjunto.add(7)
print(conjunto)
# print(conjunto[0]) Conjunto não tem ordem, então não tem índice

conjunto = {"Ana", "Carol", "Maria", "Paula"}
print(conjunto)
print(conjunto)
print(conjunto)

print()
for item in conjunto:
  print(item)

# DICIONÁRIO

dicionario = {}
dicionario = dict()

dicionario = {"Chave":"Valor", "Chave1":"Valor1"}

estados = {"SP":"São Paulo", "RJ":"Rio", "MG":"Minas"}
print()
print(estados)
for item in estados:
  print(item)

print()
for item in estados:
  print(estados[item])

print()
for chave in estados.keys():
  print(chave) 

print()
for valor in estados.values():
  print(valor) 

print()
for chave, valor in estados.items():
  print(chave, valor)

estados["RJ"] = "Rio de Janeiro"
print()
print(estados["RJ"])

estados["ES"] = "Espírito Santo"
print()
print(estados)

# Conjunto (set) x Lista

lista = []
tupla = ()
conjunto = {}

lista.append("item")
tupla # não tem como adicionar
conjunto[0] = "item"

print(conjunto)

for i in conjunto:
  print(i)

print(conjunto[0])

conjunto = set(range(0, 11))
print(conjunto)

# i = 0
# while i < len(conjunto):
#   print(conjunto[i])
#   i += 1

for item in conjunto:
  print(item)

# TUPLA x LISTA

lista_vazia = []
print(lista_vazia)
lista_vazia.append("Bom dia")
lista_vazia.append("Olá, mundo")
print(lista_vazia)

tupla = ()
print(tupla)
tupla = list(("Ana", "Paula", "Sofia"))
tupla.append("Cristal")
tupla = tuple(tupla)
print(tupla)

print(lista_vazia[0])
print(tupla[3])
 