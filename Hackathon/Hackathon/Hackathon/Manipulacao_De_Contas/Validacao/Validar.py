from rich.console import Console
console = Console()

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
                console.print("\n[bold red]CPF Invalido! Primeiro digito verificador não bateu![/bold red]")
                return False
        else:
            if int(cpfFormatado[9]) != (11 - resto):
                console.print("\n[bold red]CPF Invalido! Primeiro digito verificador não bateu[/bold red]")
                return False
        soma = float(0)
        for i in range(10):
            soma += int(cpfFormatado[i]) * (11-i)
        resto = soma%11
        if resto < 2:
            if int(cpfFormatado[10]) != 0:
                console.print("\n[bold red]CPF Invalido! Segundo digito verificador não bateu![/bold red]")
                return False
        else:
            if int(cpfFormatado[10]) != (11 - resto):
                console.print("\n[bold red]CPF Invalido! Segundo digito verificador não bateu![/bold red]")
                return False
        if cpfFormatado[0:2] == cpfFormatado[3:5] and cpfFormatado[6:8] == cpfFormatado[3:5]:
            console.print("\n[bold red]CPF Invalido! Numeros iguais[/bold red]")
            return False
    else:
        console.print("\n[bold red]CPF Invalido! Erro Desconehcido[/bold red]")
        return False
    return True

def validar_Email(email):
    if email[email.find("@")-1].isalpha() and email.find("@") > 2 and email[email.find("@")+1].isalpha():
        return True
    console.print("\n[bold red]Email Invalido![/bold red]")
    return False

def validar_telefone(telefone):
    telefone = telefone.replace(" ","")
    if telefone[0] == '(' and telefone[3] == ')' and ((len(telefone) == 13 or len(telefone) == 12) or len(telefone) == 14):
        return True
    console.print("[bold red]\nTelefone Invalido![/bold red]")
    return False

def validar_data(data):
    if len(data) == 10 and data[0:1].isdigit() and data[3:4].isdigit() and data[6:9].isdigit():
        ano = float(data[6:9])
        if (2024-ano) > 18:
            return True
        else:
            console.print("\"n[bold red]Não é possivel abrir conta para menores de idade![/bold red]")
            return False
    console.print("\n[bold red]Data Invalida![/bold red]")
    return False

def validar_senha(senha):
    if len(senha) > 8:
        if senha.find("@") != None:
            return "[bold green]Senha Forte[/bold green]"
        return "[bold yellow]Senha Razoavel[/bold yellow]"
    else:
        return "[bold red]Senha Fraca[/bold red]"

def validar_cep(cep):
    if len(cep) == 9:
        if cep[5] == '-':
            return True
    console.print("\n[bold red]Cep Invalido![/bold red]")
    return False

def validar_CNPJ(cnpj):
    cnpj = ''.join(c for c in cnpj if c.isdigit())
    if len(cnpj) != 14:
        console.print("\n[bold red]CNPJ Invalido![/bold red]")
        return False
    if cnpj == cnpj[0] * 14:
        console.print("\n[bold red]CNPJ Invalido![/bold red]")
        return False
    pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    for i in range(12):
        soma += int(cnpj[i]) * pesos_1[i]
    resto = soma % 11
    primeiro_digito = 0 if resto < 2 else 11 - resto
    soma = 0
    for i in range(13):
        soma += int(cnpj[i]) * pesos_2[i]
    resto = soma % 11
    segundo_digito = 0 if resto < 2 else 11 - resto
    if int(cnpj[12]) == primeiro_digito and int(cnpj[13]) == segundo_digito:
        return True
    console.print("\n[bold red]CNPJ Invalido![/bold red]")
    return False
