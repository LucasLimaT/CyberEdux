cadastros = list()
while True:
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu cpf: ")
    data_de_nascimento = input("Digite sua data de nascimento: ")
    sexo = input("Digite seu sexo: ")
    estadoCivil = input("Digite seu estado civil: ")
    rendaMensal = input("Digite sua renda mensal: ")
    logradouro = input("Digite seu logradouro: ")
    numero = input("Digite seu numero: ")
    complemento = input("Digite seu complemento: ")
    estado = input("Digite seu estado: ")
    cidade = input("Digite sua cidade: ")
    cadastros.append({
        "Nome": nome, 
        "CPF": cpf,
        "DataDeNascimento": data_de_nascimento,
        "Sexo": sexo,
        "EstadoCivil": estadoCivil,
        "RendaMensal": rendaMensal,
        "endereco": {
            "Logradouro": logradouro,
            "Numero": numero,
            "Complemento": complemento,
            "Estado": estado,
            "Cidade": cidade
        }
    })
    continuar = input("Deseja continuar?\n(S/N)\n").upper()
    if continuar != "S":
        break
print(cadastros)

