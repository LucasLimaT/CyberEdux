import getpass
from Manipulacao_De_Saldo_E_Extrato.Manipulacao_De_Saldo import criacao_de_saldo
from Manipulacao_De_Contas.Opcoes.Opcoes import criar_preferencias
from Manipulacao_De_Contas.Validacao import Validar
from rich.console import Console
console = Console()

def pessoa_fisica(contas):
    console.print("[bold cyan]Cadastro de Cliente[/bold cyan]")
    while True:
        documento = str(input("\nCPF:\nxxx.xxx.xxx-xx\n")).strip()
        if Validar.validar_CPF(documento) == True:
            if not encontrar_cliente(contas, documento):
                break
            console.print("\n[bold red]Documento já cadastrado![/bold red]")
    while True:
        email = input("\nEMAIL: ").strip()
        if Validar.validar_Email(email) == True:
            break
    while True:
        telefone = input("\nTELEFONE:\n(xx) xxxx-xxxx\n").strip()
        if Validar.validar_telefone(telefone) == True:
            break
    while True:
        data = input("\nDATA DE NASCIMENTO:\ndd/mm/yyyy\n").strip()
        if Validar.validar_data(data) == True:
            break
    while True:
        cep = str(input("\nCEP: ")).strip()
        if Validar.validar_cep(cep) == True:
            break
    estado = str(input("\nUF: ")).strip().upper()
    pais = str(input("\nPAÍS: ")).strip().lower()
    pais = pais.capitalize()
    cidade = str(input("\nCIDADE: ")).strip().lower()
    cidade = cidade.capitalize()
    logradouro = str(input("\nLOGRADOURO: ")).strip().lower()
    logradouro = logradouro.capitalize()
    numero = input("\nNUMERO: ").strip()
    bairro = str(input("\nBAIRRO: ")).strip().lower()
    bairro = bairro.capitalize()
    nome = str(input("\nNOME COMPLETO DO TITULAR: ")).strip().lower()
    nome = nome.capitalize()
    senha = getpass.getpass("\nSENHA: ").strip()
    texto = Validar.validar_senha(senha)
    while True:
        console.print(texto)
        if texto == "[bold red]Senha Fraca[/bold red]":
            senha = input("Forneca uma senha mais forte:\n").strip()
            texto = Validar.validar_senha(senha)
        else:
            break
    while True:
        opcao = getpass.getpass("\nQual tipo de conta deseja abrir?\n[1] Conta Corrente\t[2] Conta Poupanca\n")
        if opcao == "1":
            tipo = "Conta Corrente"
            break
        elif opcao == "2":
            tipo = "Conta Poupanca"
            break
    conta = {
            "documento": documento,
            "email": email,
            "telefone": telefone,
            "data": data,
            "endereco": {
                "pais": pais,
                "cep": cep,
                "uf": estado,
                "cidade": cidade,
                "logradouro": logradouro,
                "numero": numero,
                "bairro": bairro
            },
            "nome": nome,
            "senha": senha,
            "tipo": tipo
            }
    return conta

def pessoa_juridica(contas):
    console.print("[bold cyan]Cadastro de Empresa[/bold cyan]")
    while True:
        documento = str(input("\nCNPJ:\nxx.xxx.xxx/xxxx-xx\n")).strip()
        if Validar.validar_CNPJ(documento) == True:
            if not encontrar_cliente(contas, documento):
                break
            console.print("\n[bold red]Documento já cadastrado![/bold red]")
    while True:
        telefone_empresa = input("\nTELEFONE DA EMPRESA:\n(xx) xxxx-xxxx\n").strip()
        if Validar.validar_telefone(telefone_empresa) == True:
            break
    razao_social = str(input("\nRAZAO SOCIAL: ")).strip().lower()
    razao_social = razao_social.capitalize()
    print("\n--- Endereço da Empresa ---")
    while True:
        cep = str(input("\nCEP: ")).strip()
        if Validar.validar_cep(cep) == True:
            break
    estado = str(input("\nUF: ")).strip().upper()
    cidade = str(input("\nCIDADE: ")).strip().lower()
    cidade = cidade.capitalize()
    logradouro = str(input("\nLOGRADOURO: ")).strip().lower()
    logradouro = logradouro.capitalize()
    numero = input("\nNUMERO: ").strip()
    bairro = str(input("\nBAIRRO: ")).strip().lower()
    bairro = bairro.capitalize()
    print("\n--- Dados do Representante Legal ---")
    nome = str(input("\nNOME COMPLETO: ")).strip().lower()
    nome = nome.capitalize()
    while True:
        cpf = str(input("\nCPF:\nxxx.xxx.xxx-xx\n")).strip()
        if Validar.validar_CPF(cpf) == True:
            break
    while True:
        telefone = input("\nTELEFONE:\n(xx) xxxx-xxxx\n").strip()
        if Validar.validar_telefone(telefone) == True:
            break
    while True:
        email = input("\nEMAIL: ").strip()
        if Validar.validar_Email(email) == True:
            break
    senha = getpass.getpass("\nSENHA: ").strip()
    texto = Validar.validar_senha(senha)
    while True:
        console.print(texto)
        if texto == "[bold red]Senha Fraca[/bold red]":
            senha = input("Forneca uma senha mais forte:\n").strip()
            texto = Validar.validar_senha(senha)
        else:
            break
    conta = {
        "documento": documento,
        "nome": razao_social,
        "telefone": telefone_empresa,
        "endereco": {
            "logradouro": logradouro,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "uf": estado,
            "cep": cep
        },
        "Responsavel": {
            "nome_responsavel": nome,
            "cpf_responsavel": cpf,
            "telefone_responsavel": telefone,
            "email_responsavel": email
        },
        "senha": senha,
        "tipo": "Conta Empresa"
    }
    return conta

def cadastro(contas, preferencias, saldos):
    try:
        while True:
            opcao = getpass.getpass("\nDeseja abrir uma conta Pessoa Fisica ou Pessoa Juridica?\n[1] Pessoa Fisica\t[2] Pessoa Juridica\n")
            if opcao == "1":
                conta = pessoa_fisica(contas)
                preferencia = criar_preferencias(conta)
                break
            elif opcao == "2":
                conta = pessoa_juridica(contas)
                preferencia = criar_preferencias(conta)
                break
            else:
                print("Opcao Invalida!")
                continue
        contas.append(conta)
        preferencias.append(preferencia)
        criacao_de_saldo(conta, saldos)
        console.print("[bold cyan3 ]Cliente cadastrado com sucesso![/bold cyan3]")
        return
    except Exception as ex:
        console.print(f"[bold red]Erro ao fazer cadastro: {ex}[/bold red]")
        return
    
def encontrar_cliente(contas, documento):
    try:
        for cliente in contas:
            if cliente["documento"] == documento:
                return cliente
        return None
    except Exception as e:
        console.print("[bold red] Não existe cliente[/bold red]", e)

def encontrar_cliente_telefone(contas, telefone):
    try:
        for cliente in contas:
            if isinstance(cliente, dict):
                tipo = cliente.get("tipo")
                if tipo != "Conta Empresa" and cliente.get("telefone") == telefone:
                    return cliente
        return None
    except Exception as e:
        console.print(f"[bold red]Erro ao procurar cliente com email {telefone}[/bold red]: {e}")
        return None

def encontrar_cliente_email(contas, email):
    try:
        for cliente in contas:
            if isinstance(cliente, dict):
                tipo = cliente.get("tipo")  
                if tipo != "Conta Empresa" and cliente.get("email") == email:
                    return cliente
        return None
    except Exception as e:
        console.print(f"[bold red]Erro ao procurar cliente com email {email}[/bold red]: {e}")
        return None