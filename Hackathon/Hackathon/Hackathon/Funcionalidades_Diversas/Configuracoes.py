from Manipulacao_De_Contas.Validacao.Validar import validar_Email, validar_senha, validar_telefone
from Manipulacao_De_Contas.Opcoes.Opcoes import atualiza_preferencias, encontrar_preferencias
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
console = Console()

def mudar_moeda_padrao(preferencia, preferencias):
    console.print("[bold gray]Mudar Moeda Padrao[/bold gray]")
    if preferencia["moeda_padrao"] == "BRL": 
        console.print("Para qual moeda deseja fazer a alteração?")
        console.print("1. Dolar")
        console.print("2. Euro")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            preferencia["moeda_padrao"] = "USD"
        elif opcao == "2":
            preferencia["moeda_padrao"] = "EUR"
    elif preferencia["moeda_padrao"] == "USD": 
        console.print("Para qual moeda deseja fazer a alteração?")
        console.print("1. BRL")
        console.print("2. Euro")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            preferencia["moeda_padrao"] = "BRL"
        elif opcao == "2":
            preferencia["moeda_padrao"] = "EUR"
    elif preferencia["moeda_padrao"] == "EUR": 
        console.print("Para qual moeda deseja fazer a alteração?")
        console.print("1. BRL")
        console.print("2. Dolar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            preferencia["moeda_padrao"] = "BRL"
        elif opcao == "2":
            preferencia["moeda_padrao"] = "USD"
    else:
        console.print("[bold red]Opção inválida![/bold red]")
        return
    atualiza_preferencias(preferencia, preferencias)
    console.print("[bold green]Moeda alterada com sucesso![/bold green]")

def mudar_nome_preferencia(preferencia, preferencias):
    console.print("[bold gray]Mudar Nome Pelo Qual Quer Ser Chamado[/bold gray]")
    console.print(f"Nome atual: {preferencia["nome_chamado"]}")
    novo_nome = input("Novo nome: ")
    if not novo_nome:
        return
    preferencia["nome_chamado"] = novo_nome
    atualiza_preferencias(preferencia, preferencias)
    console.print(f"[bold green]Nome alterado com sucesso![/bold green]")

def atualizar_dados(usuario_logado, contas):

    console.print("[bold gray]O que deseja mudar?[/bold gray]")
    console.print("1. Email")
    console.print("2. Telefone")
    console.print("3. Endereco")
    console.print("4. Senha")
    console.print("0. Voltar")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        alterar_email(usuario_logado)
        atualiza_dados_da_conta(usuario_logado, contas)
    elif opcao == "2":
        alterar_telefone(usuario_logado)
        atualiza_dados_da_conta(usuario_logado, contas)
    elif opcao == "3":
        alterar_endereco(usuario_logado)
        atualiza_dados_da_conta(usuario_logado, contas)
    elif opcao == "4":
        alterar_senha(usuario_logado)
        atualiza_dados_da_conta(usuario_logado, contas)
    elif opcao == "0":
        return
    else:
        console.print("[bold red]Opção inválida![/bold red]")
    return

def alterar_senha(conta):
    while True:
        nova_senha = input("Digite a nova senha: ")
        confirmar_senha = input("Confirme a nova senha: ")
        verifica = validar_senha(nova_senha)
        if verifica == "Senha Forte":
            break
        else:
            console.print(verifica)
    if nova_senha == confirmar_senha:
        conta["senha"] = nova_senha
        console.print("[bold green]Senha alterada com sucesso.[/bold green]")
    else:
        console.print("[bold red]As senhas não coincidem. Tente novamente.[/bold red]")
    return

def alterar_telefone(conta):
    while True:
        novo_telefone = input("Digite o novo telefone: ")
        if validar_telefone(novo_telefone):
            break
    conta["telefone"] = novo_telefone
    console.print("[bold green]Telefone alterado com sucesso.[/bold green]")
    return 

def alterar_endereco(conta):
    print("Digite os novos dados de endereço:")
    pais = input("País: ")
    cep = input("CEP: ")
    estado = input("Estado (UF): ")
    cidade = input("Cidade: ")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    novo_endereco = {
        "pais": pais,
        "cep": cep,
        "uf": estado,
        "cidade": cidade,
        "logradouro": logradouro,
        "numero": numero,
        "bairro": bairro
    }
    conta["endereco"] = novo_endereco
    console.print("[bold green]Endereço alterado com sucesso.[/bold green]")
    return

def alterar_email(conta):
    if conta["tipo"] != "Conta Empresa":
        while True:
            novo_email = input("Digite o novo email: ")
            if validar_Email(novo_email):
                break
        conta["email"] = novo_email
        console.print("[bold green]Email alterado com sucesso.[/bold green]")
    else:
        print("[bold red]Conta do tipo 'empresa' não pode ter email alterado.[/bold red]")
    return

def consultar_dados(usuario_logado):
    try:
        if usuario_logado["tipo"] == "Conta Empresa":
            table = Table(title="Dados da Conta PJ", show_header=True, header_style="bold magenta")
            table.add_column("Campo", style="dim", width=20)
            table.add_column("Valor", justify="left")
            table.add_row("Documento", usuario_logado["documento"])
            table.add_row("Razão Social", usuario_logado["nome"])
            table.add_row("Telefone", usuario_logado["telefone"])
            table.add_row("Endereço", f"{usuario_logado['endereco']['logradouro']}, {usuario_logado['endereco']['numero']} - {usuario_logado['endereco']['bairro']}, {usuario_logado['endereco']['cidade']} - {usuario_logado['endereco']['uf']}, {usuario_logado['endereco']['cep']}")
            table.add_row("Responsável", usuario_logado["Responsavel"]["nome_responsavel"])
            table.add_row("CPF do Responsável", usuario_logado["Responsavel"]["cpf_responsavel"])
            table.add_row("Telefone do Responsável", usuario_logado["Responsavel"]["telefone_responsavel"])
            table.add_row("Email do Responsável", usuario_logado["Responsavel"]["email_responsavel"])
            table.add_row("Senha", usuario_logado["senha"])
            console.print(Panel(table, title="Conta PJ", title_align="center"))
        elif usuario_logado["tipo"] == "Conta Corrente" or usuario_logado["tipo"] == "Conta Poupanca":
            table = Table(title="Dados da Conta PF", show_header=True, header_style="bold cyan")
            table.add_column("Campo", style="dim", width=20)
            table.add_column("Valor", justify="left")
            table.add_row("Documento", usuario_logado["documento"])
            table.add_row("Nome", usuario_logado["nome"])
            table.add_row("Email", usuario_logado["email"])
            table.add_row("Telefone", usuario_logado["telefone"])
            table.add_row("Endereço", f"{usuario_logado['endereco']['logradouro']}, {usuario_logado['endereco']['numero']} - {usuario_logado['endereco']['bairro']}, {usuario_logado['endereco']['cidade']} - {usuario_logado['endereco']['uf']}, {usuario_logado['endereco']['cep']}")
            table.add_row("Senha", usuario_logado["senha"])
            console.print(Panel(table, title="Conta PF", title_align="center"))
    except:
        console.print("[bold red]Ops! Algum imprevisto aconteceu![/bold red]")

def excluir_conta(usuario_logado, contas):
    certeza = console.input('[bold red]⚠️  TEM CERTEZA QUE QUER FAZER ISSO?⚠️\n SE SIM DIGITE "QUERO" MAIUSCULO, CASO CONTRARIO APERTE ENTER[/bold red]')
    if not certeza:
        return
    elif certeza == "QUERO":
        aux = usuario_logado["documento"]
        usuario_logado["documento"] = "Conta_Exlcuida"
        for i in contas:
            if i["documento"] == aux:
                pos = contas.index(i)
                contas[pos] = usuario_logado
                break
    else:
        return
    return

def atualiza_dados_da_conta(conta, contas): 
    for i in contas:
        if i["documento"] == conta["documento"]:
            pos = contas.index(i)
            contas[pos] = conta
            break
    return