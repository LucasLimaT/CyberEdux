def validar_CPF(cpf):
    cpfFormatado = str("")
    soma = float(0)
    for i in range(len(cpf)): 
        if cpf[i].isdigit():
            cpfFormatado += cpf[i]
    if len(cpfFormatado) == 11:
        for i in range(9):
            soma += int(cpfFormatado[i]) * (10-i)
        resto = soma%11
        if resto < 2:
            if cpfFormatado[9] != 0:
                print("\nCPF Invalido! Primeiro digito verificador não bateu!")
                return False
        else:
            if int(cpfFormatado[9]) != (11 - resto):
                print("\nCPF Invalido! Primeiro digito verificador não bateu")
                return False
        soma = float(0)
        for i in range(10):
            soma += int(cpfFormatado[i]) * (11-i)
        resto = soma%11
        if resto < 2:
            if int(cpfFormatado[10]) != 0:
                print("\nCPF Invalido! Segundo digito verificador não bateu!")
                return False
        else:
            if int(cpfFormatado[10]) != (11 - resto):
                print("\nCPF Invalido! Segundo digito verificador não bateu!")
                return False
        if cpfFormatado[0:2] == cpfFormatado[3:5] and cpfFormatado[6:8] == cpfFormatado[3:5]:
            print("\nCPF Invalido! Numeros iguais")
            return False
    else:
        print("\nCPF Invalido! Erro Desconehcido")
        return False
    return True

def validar_Email(email):
    if email[email.find("@")-1].isalpha() and email.find("@") > 2 and email[email.find("@")+1].isalpha():
        return True
    print("\nEmail Invalido!")
    return False

def validar_telefone(telefone):
    telefone = telefone.replace(" ","")
    if telefone[0] == '(' and telefone[3] == ')' and ((len(telefone) == 13 or len(telefone) == 12) or len(telefone) == 14):
        return True
    print("\nTelefone Invalido!")
    return False

def validar_data(data):
    if len(data) == 10 and data[0:1].isdigit() and data[3:4].isdigit() and data[6:9].isdigit():
        return True
    print("\nData Invalida!")
    return False

def validar_senha(senha):
    if len(senha) > 8:
        if senha.find("@") != None:
            return "Senha Forte"
        return "Senha Razoavel"
    else:
        return "Senha Fraca"