from Manipulacao_De_Saldo_E_Extrato.Deposito_e_Saque.DepositoESaque import verifica_moeda_padrao
from Manipulacao_De_Saldo_E_Extrato.Manipulacao_De_Saldo import atualiza_saldo, procura_saldo
from Manipulacao_De_Contas.Opcoes.Opcoes import encontrar_preferencias
from rich.console import Console
console = Console()

def comprar_cambio(usuario_logado, preferencias, saldos):
    try:
        preferencia = encontrar_preferencias(preferencias, usuario_logado["documento"])
        saldo = procura_saldo(usuario_logado, preferencias, saldos)
        taxas_venda_Real = {"USD": 0.10, "EUR": 0.13}
        taxas_venda_Dolar = {"BRL": 6.0, "EUR": 0.85}
        taxas_venda_Euro = {"BRL": 6.3, "USD": 0.99}
        console.print("[bold cyan]Comprar Cambio[/bold cyan]")
        if preferencia["moeda_padrao"] == "BRL": 
            console.print("Qual moeda deseja comprar?")
            console.print(f"1. Dolar (Preço de venda: US$ {taxas_venda_Real["USD"]})")
            console.print(f"2. Euro (Preço de venda: € {taxas_venda_Real["EUR"]})")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                nova_moeda = "USD"
                valor = pegar_valor_venda(preferencia["moeda_padrao"], saldo)
                if not valor:
                    return
                saldo_atualizado = procura_saldo_troca(usuario_logado, nova_moeda, saldos)
                saldo_atualizado["saldo"] += valor*taxas_venda_Real["USD"]
                saldo -= valor*taxas_venda_Real["USD"]
                atualiza_saldo(saldos, saldo)
                atualiza_saldo(saldos, saldo_atualizado)
                console.print("[bold green]Compra realizada com sucesso![/bold green]")
                return
            elif opcao == "2":
                nova_moeda = "EUR"
                valor = pegar_valor_venda(preferencia["moeda_padrao"], saldo)
                if not valor:
                    return
                saldo_atualizado = procura_saldo_troca(usuario_logado, nova_moeda, saldos)
                saldo_atualizado["saldo"] += valor*taxas_venda_Real["EUR"]
                saldo -= valor*taxas_venda_Real["EUR"]
                atualiza_saldo(saldos, saldo)
                atualiza_saldo(saldos, saldo_atualizado)
                console.print("[bold green]Compra realizada com sucesso![/bold green]")
                return
            else:
                console.print("[bold red]Opcao inválida![/bold red]")
        elif preferencia["moeda_padrao"] == "USD": 
            console.print("Qual moeda deseja comprar?")
            console.print(f"1. Real (Preço de venda: R$ {taxas_venda_Dolar["BRL"]})")
            console.print(f"2. Euro (Preço de venda: € {taxas_venda_Dolar["EUR"]})")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                nova_moeda = "BRL"
                valor = pegar_valor_venda(preferencia["moeda_padrao"], saldo)
                if not valor:
                    return
                saldo_atualizado = procura_saldo_troca(usuario_logado, nova_moeda, saldos)
                saldo_atualizado["saldo"] += valor*taxas_venda_Dolar["BRL"]
                saldo -= valor*taxas_venda_Dolar["BRL"]
                atualiza_saldo(saldos, saldo)
                atualiza_saldo(saldos, saldo_atualizado)
                console.print("[bold green]Compra realizada com sucesso![/bold green]")
                return
            elif opcao == "2":
                nova_moeda = "EUR"
                valor = pegar_valor_venda(preferencia["moeda_padrao"], saldo)
                if not valor:
                    return
                saldo_atualizado = procura_saldo_troca(usuario_logado, nova_moeda, saldos)
                saldo_atualizado["saldo"] += valor*taxas_venda_Dolar["EUR"]
                saldo -= valor*taxas_venda_Dolar["EUR"]
                atualiza_saldo(saldos, saldo)
                atualiza_saldo(saldos, saldo_atualizado)
                console.print("[bold green]Compra realizada com sucesso![/bold green]")
                return
            else:
                console.print("[bold red]Opcao inválida![/bold red]")
        else:
            console.print("Qual moeda deseja comprar?")
            console.print(f"1. Real (Preço de venda: R$ {taxas_venda_Euro["BRL"]})")
            console.print(f"1. Dolar (Preço de venda: US$ {taxas_venda_Euro["USD"]})")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                nova_moeda = "BRL"
                valor = pegar_valor_venda(preferencia["moeda_padrao"], saldo)
                if not valor:
                    return
                saldo_atualizado = procura_saldo_troca(usuario_logado, nova_moeda, saldos)
                saldo_atualizado["saldo"] += valor*taxas_venda_Euro["BRL"]
                saldo -= valor*taxas_venda_Euro["BRL"]
                atualiza_saldo(saldos, saldo)
                atualiza_saldo(saldos, saldo_atualizado)
                console.print("[bold green]Compra realizada com sucesso![/bold green]")
                return
            elif opcao == "2":
                nova_moeda = "USD"
                valor = pegar_valor_venda(preferencia["moeda_padrao"], saldo)
                if not valor:
                    return
                saldo_atualizado = procura_saldo_troca(usuario_logado, nova_moeda, saldos)
                saldo_atualizado["saldo"] += valor*taxas_venda_Euro["USD"]
                saldo -= valor*taxas_venda_Euro["USD"]
                atualiza_saldo(saldos, saldo)
                atualiza_saldo(saldos, saldo_atualizado)
                console.print("[bold green]Compra realizada com sucesso![/bold green]")
                return
            else:
                console.print("[bold red]Opcao inválida![/bold red]")
    except:
        console.print("[bold red]Algo deu errado na troca de cambio![/bold red]")
        return

def pegar_valor_venda(moeda, saldo):
    valor = float(input(f"Forneça quando você deseja gastar: {verifica_moeda_padrao(saldo["moeda_padrao"])}"))
    if valor <= 0:
        console.print("[bold red]Valor inválido![/bold red]")
        return None
    return valor

def procura_saldo_troca(conta, nova_moeda, saldos):
    try:
        for saldo in saldos:
            if saldo["usuario"] == conta["documento"] and saldo["moeda_padrao"] == nova_moeda:
                return saldo
        return None
    except Exception as e:
        print(f"Erro ao procurar saldo: {e}")