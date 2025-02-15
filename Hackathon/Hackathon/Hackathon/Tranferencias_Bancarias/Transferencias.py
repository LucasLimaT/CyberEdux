from datetime import datetime
from Manipulacao_De_Saldo_E_Extrato.Deposito_e_Saque.DepositoESaque import verifica_moeda_padrao
from Manipulacao_De_Saldo_E_Extrato.Manipulacao_De_Saldo import atualiza_saldo, procura_saldo, procura_saldo_destinatario
from Manipulacao_De_Contas.Cadastro.Cadastro import encontrar_cliente, encontrar_cliente_email, encontrar_cliente_telefone
from rich.console import Console
console = Console()

def transferencia_TED(clientes, cliente, opcoes, saldos):
    try:
        console.print("[bold cyan3]Transferência[/bold cyan3]")
        documento_destino = input("Documento do destinatário: ")
        destinatario = encontrar_cliente(clientes, documento_destino)
        if not destinatario:
            console.print("[bold red]Destinatário não encontrado![/bold red]")
            return saldos
        saldo_destinatario = procura_saldo_destinatario(destinatario, opcoes, saldos, cliente)
        saldo_cliente = procura_saldo(cliente, opcoes, saldos)
        valor = float(input(f"Valor a transferir: {verifica_moeda_padrao(saldo_cliente["moeda_padrao"])}"))
        if valor <= 0 or valor > saldo_cliente["saldo"]:
            console.print("[bold red]Saldo insuficiente ou valor inválido![/bold red]")
            return saldos
        saldo_cliente["saldo"] -= valor
        saldo_destinatario["saldo"] += valor
        saldo_cliente["extratos"].append((datetime.now(), f"Transferência para {destinatario["nome"]}",  -valor))
        saldo_destinatario["extratos"].append((datetime.now(), f"Transferência de {cliente["nome"]}", valor))
        atualiza_saldo(saldos, saldo_cliente)
        atualiza_saldo(saldos, saldo_destinatario)
        console.print("[bold green]Transferência realizada com sucesso![/bold green]")
        return saldos
    except:
        console.print("[bold red]Ocorreu alguma falha ao executar a transferencia![/bold red]")
        return saldos

def pix(clientes, cliente, opcoes, saldos):
    try:
        console.print("[bold cyan3]PIX[/bold cyan3]")
        chave = input("Chave: ")
        destinatario = verifica_chave_pix(clientes, chave)
        if not destinatario:
            console.print("[bold red]Destinatário não encontrado![/bold red]")
            return saldos
        saldo_destinatario = procura_saldo_destinatario(destinatario, opcoes, saldos, cliente)
        saldo_cliente = procura_saldo(cliente, opcoes, saldos)
        valor = float(input(f"Valor do pix: {verifica_moeda_padrao(saldo_cliente["moeda_padrao"])}"))
        if valor <= 0 or valor > saldo_cliente["saldo"]:
            console.print("[bold red]Saldo insuficiente ou valor inválido![/bold red]")
            return saldos
        saldo_cliente["saldo"] -= valor
        saldo_destinatario["saldo"] += valor
        saldo_cliente["extratos"].append((datetime.now(), f"Pix para {destinatario["nome"]}", -valor))
        saldo_destinatario["extratos"].append((datetime.now(), f"Pix de {cliente["nome"]}", valor))
        atualiza_saldo(saldos, saldo_cliente)
        atualiza_saldo(saldos, saldo_destinatario)
        console.print("[bold green]Pix realizada com sucesso![/bold green]")
        return saldos
    except:
        console.print("[bold red]Ocorreu alguma falha ao executar o pix![/bold red]")
        return saldos

def verifica_chave_pix(clientes, chave):
    destinatario = encontrar_cliente(clientes, chave)
    if not destinatario:
        destinatario = encontrar_cliente_telefone(clientes, chave)
        if not destinatario:
            destinatario = encontrar_cliente_email(clientes, chave)
    return destinatario

def menu_transferencias(cliente, clientes, opcoes, saldos):
    try:
        while True:
            console.print("\n[bold yellow]Transferencias Bancarias[/bold yellow]")
            console.print("1. TED")
            console.print("2. PIX")
            console.print("0. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                transferencia_TED(clientes, cliente, opcoes, saldos)
            elif opcao == "2":
                pix(clientes, cliente, opcoes, saldos)
            elif opcao == "0":
                return
            else:
                console.print("[bold red]Opção inválida![/bold red]")
    except:
        console.print("[bold red]Ops! Algum imprevisto aconteceu![/bold red]")
        return saldos