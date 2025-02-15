def lista_normal():
    i = int(1)
    lista = list()
    while True:
        lista.append(input(f"Nome do {i}º aluno: "))
        lista.append(float(input(f"Qual a 1º Nota do {lista[3*(i-1)]}: ")))
        lista.append(float(input(f"Qual a 2º Nota do {lista[3*(i-1)]}: ")))
        lista.append(float(input(f"Qual a 3º Nota do {lista[3*(i-1)]}: ")))
        i += 1
        opcao = input("Deseja continuar? (S/N)")
        if opcao.upper() == "N":
            break
    return lista


def criacao_tupla(nome, notas):
    return (nome, notas[0], notas[1], notas[2])

def lista_tupla_lista():
    lista = []
    while True:
        notas = []
        nome = input("Digite um nome: ")
        notas.append(float(input("Digite a 1ª nota: ")))
        notas.append(float(input("Digite a 2ª nota: ")))
        notas.append(float(input("Digite a 3ª nota: ")))
        lista.append(criacao_tupla(nome, notas))
        opcao = input("Deseja continuar? (S/N)")
        if opcao.upper() == "N":
            break
    return lista

def criacao_dicionario(nome, notas):
    dicionario = {nome: notas}
    return dicionario

def lista_de_dicionarios():
    dicionario = []
    while True:
        notas = []
        nome = input("Digite um nome: ")
        notas.append(float(input("Digite a 1ª nota: ")))
        notas.append(float(input("Digite a 2ª nota: ")))
        notas.append(float(input("Digite a 3ª nota: ")))
        dicionario.append(criacao_dicionario(nome, notas))
        opcao = input("Deseja continuar? (S/N)")
        if opcao.upper() == "N":
            break
    return dicionario


def dicionario_com_lista():
    dicionario = {}
    while True:
        notas = []
        nome = input("Digite um nome: ")
        notas.append(float(input("Digite a 1ª nota: ")))
        notas.append(float(input("Digite a 2ª nota: ")))
        notas.append(float(input("Digite a 3ª nota: ")))
        dicionario[nome] = notas
        opcao = input("Deseja continuar? (S/N)")
        if opcao.upper() == "N":
            break
    return dicionario

variavel = lista_normal()
i = int(1)
j = int(0)
'''print(f"Lista Normal:\n {variavel}")
while i < len(variavel):
    print(f"Nome: {variavel[j]} - Notas: {variavel[i]}")
    i+=1
    if i%4 == 0:
        j+=3
        i+=1
        if j > len(variavel):
            break
variavel = lista_tupla_lista()'''
print(f"Lista com Tupla:\n {variavel}")
for i in range(len(variavel)):
    print(f"Nome: {variavel[i][0]} - Notas: {variavel[i][1]},{variavel[i][2]},{variavel[i][3]}")
#print(f"Dicionario com lista:\n {dicionario_com_lista()}")
#print(f"Lista de dicionarios:\n {lista_de_dicionarios()}")