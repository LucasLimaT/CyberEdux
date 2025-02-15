from Investimentos.Investimentos import formatar_valor
from Manipulacao_De_Saldo_E_Extrato.Deposito_e_Saque.DepositoESaque import depositar, sacar
from Manipulacao_De_Contas.Opcoes.Opcoes import encontrar_preferencias
from rich.console import Console
console = Console()

def criacao_de_saldo(conta, saldos):
    try:
        saldo_em_brl = {
            "usuario": conta["documento"],
            "moeda_padrao": "BRL",
            "saldo": 0.0,
            "extratos": []
        }
        saldo_em_eur = {
            "usuario": conta["documento"],
            "moeda_padrao": "EUR",
            "saldo": 0.0,
            "extratos": []
        }
        saldo_em_dol = {
            "usuario": conta["documento"],
            "moeda_padrao": "USD",
            "saldo": 0.0,
            "extratos": []
        }
        saldos.append(saldo_em_brl)
        saldos.append(saldo_em_dol)
        saldos.append(saldo_em_eur)
        return saldos
    except:
        console.print("[bold red]Erro ao manipular saldo![/bold red]")

def menu_saldo_deposito_saque(conta, opcoes, saldos):
    try:
        while True:
            console.print("\n[bold yellow]Saldo e Deposito[/bold yellow]")
            console.print("1. Deposito")
            console.print("2. Saque")
            console.print("0. Voltar")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                saldo = procura_saldo(conta, opcoes, saldos)
                saldo = depositar(saldo)
                atualiza_saldo(saldos, saldo)
            elif opcao == "2":
                saldo = procura_saldo(conta, opcoes, saldos)
                saldo = sacar(saldo)
                atualiza_saldo(saldos, saldo)
            elif opcao == "0":
                return
            else:
                console.print("[bold red]Opção inválida![/bold red]")
    except:
        console.print("[bold red]Ops! Algum imprevisto aconteceu![/bold red]")
        return saldos

def procura_saldo(conta, opcoes, saldos):
    try:
        opcao = encontrar_preferencias(opcoes, conta["documento"])
        for saldo in saldos:
            if saldo["usuario"] == conta["documento"] and saldo["moeda_padrao"] == opcao["moeda_padrao"]:
                return saldo
        return None
    except Exception as e:
        print(f"Erro ao procurar saldo: {e}")

def procura_saldo_destinatario(destinatario, opcoes, saldos, origem):
    opcao = encontrar_preferencias(opcoes, origem["documento"])
    for saldo in saldos:
        if saldo["usuario"] == destinatario["documento"] and saldo["moeda_padrao"] == opcao["moeda_padrao"]:
            return saldo
    return None

def atualiza_saldo(saldos, saldo): 
    for i in saldos:
        if i["usuario"] == saldo["usuario"] and i["moeda_padrao"] == saldo["moeda_padrao"]:
            pos = saldos.index(i)
            saldos[pos] = saldo
            break
    return

def consultar_saldo(cliente, opcoes, saldos):
    saldo = procura_saldo(cliente, opcoes, saldos)
    preferencia = encontrar_preferencias(opcoes, cliente["documento"])
    return f"Saldo atual: [bold green]{formatar_valor(saldo["saldo"], preferencia["moeda_padrao"])}[/bold green]"
