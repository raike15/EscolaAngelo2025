# EXERCÍCIOS WHILE

#  1. Adivinhação de números:
#  • Criem uma lista com 10 números.
#  • Peçam ao usuário para adivinhar um número da lista.
#  • Usem um loop while para continuar pedindo adivinhações até que o usuário acerte.
numeros = [10,4,7,8,0,3,6,9,2,1,5]
acertou = False
while not acertou:
    palpite = int (input("Adivinhe um número da lista: "))
    if palpite in numeros:
        print("Parabéns! Você acertou o número.")
        acertou = True
    else:
        print("Não foi dessa vez. Tente novamente!")
#  2. Contagem regressiva:
#  • Criem uma lista de contagem regressiva de 10 a 1.
#  • Usem um loop while para imprimir cada número da lista
Contagem_regressiva = [10,9,8,7,6,5,4,3,2,1]
i = 0 
while i < len(Contagem_regressiva):
    print(Contagem_regressiva[i])
# 3. Adição de números:
#  • Criem uma lista vazia para armazenar números.
#  • Peçam ao usuário para fornecer números e os adicionem à lista.
#  • Continuem pedindo números até que o usuário decida parar.
numeros = []
while True:
    entrada = input("Digite um numero para adicionar à lista ou 'parar' para encerrar.")
    if entrada.lower() == 'parar':
        break
    try:
        numeros = float(entrada)
        numeros.append(numeros)
    except ValueError:
        print("Por favor, digite um número válido ou 'parar' para encerrar.")
print("Os números adicionados foram;".numeros)
#  4.Média de notas:
#  • Criem uma lista vazia para armazenar notas.
#  • Peçam ao usuário para fornecer notas e as adicionem à lista.
#  • Calculem e imprimam a média das notas quando o usuário decidir parar
notas = []
while True:
    notas = input("Digite uma nota (ou 'parar' para terminar):")
    if notas.lower() == 'parar':
        break
    try:
        notas = float(notas)
# 5.Busca em lista:
#  • Criem uma lista de cinco nomes.
#  • Peçam ao usuário para digitar um nome.
#  • Usem um loop while para verificar se o nome está na 
# lista e informar o resultado.
nomes = ["ana", "carlos", "joão", "maria", "pedro"]
nomes_digitando = input("Dígite um nome para procurar na lista:")
while True:
    if nomes_digitando in nomes:
        print(f"O nome {nomes_digitando} está na lista!")
        break
    else:
        print(f"O nome {nomes_digitando}não está na lista.")
        nomes_digitando = input("Digite outro nome para tentar novamente:")
#  6. Contador de números:
#  • Solicitem ao usuário um número inicial.
#  • Usem um loop while para imprimir os números de 1 até o 
# número fornecido pelo usuário.
#  • Exibam uma mensagem indicando que o loop terminou solicidar um número inicial ao usúario.
numero_inicial = int(input("Digite um numero inicial:"))
contador = 1
while contador <= numero_inicial:
    print(contador)
    contador += 1 
    print("O loop terminou!")