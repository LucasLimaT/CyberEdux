import getpass
from Manipulacao_De_Contas.Opcoes.Opcoes import encontrar_preferencias
from Manipulacao_De_Saldo_E_Extrato.Manipulacao_De_Saldo import consultar_saldo, procura_saldo
from Investimentos.Investimentos import formatar_valor
from datetime import datetime
from rich.console import Console
from rich.table import Table
console = Console()

def exibir_extrato(cliente, opcoes, saldos):
    try:
        console.print("[bold cyan]Extrato[/bold cyan]")
        preferencia = encontrar_preferencias(opcoes, cliente["documento"])
        if preferencia["exibir_saldo"] == True:
            console.print(f"0. Voltar\t1. Filtrar\t{consultar_saldo(cliente, opcoes, saldos)}")
        else:
            console.print(f"0. Voltar\t1. Filtrar")
        tabela = Table(title = "Extrato")
        tabela.add_column("Data", justify = "left")
        tabela.add_column("Descrição", justify = "left")
        tabela.add_column("Valor", justify = "right")
        saldo = procura_saldo(cliente, opcoes, saldos)
        for data, descricao, valor in saldo["extratos"]:
            tabela.add_row(data.strftime("%Y-%m-%d %H:%M:%S"), descricao, formatar_valor(valor, preferencia["moeda_padrao"]))
        console.print(tabela)
        menu_extrato(cliente, opcoes, saldos)
    except:
        console.print("[bold red]Ops! Algum imprevisto aconteceu![/bold red]")

def exibir_extrato_filtro_data(cliente, opcoes, saldos):
    try:
        console.print("[bold cyan]Extrato filtrado por data[/bold cyan]")
        preferencia = encontrar_preferencias(opcoes, cliente["documento"])
        if preferencia["exibir_saldo"] == True:
            console.print(f"0. Voltar\t1. Filtrar\t{consultar_saldo(cliente, opcoes, saldos)}")
        else:
            console.print(f"0. Voltar\t1. Filtrar")
        inicio = None
        fim = None
        while not inicio and not fim:
            inicio = input("Data de início (YYYY-MM-DD): ")
            fim = input("Data de fim (YYYY-MM-DD): ")
        inicio = datetime.strptime(inicio, "%Y-%m-%d")
        fim = datetime.strptime(fim, "%Y-%m-%d")
        tabela = Table(title = "Extratos")
        tabela.add_column("Data", justify = "left")
        tabela.add_column("Descrição", justify = "left")
        tabela.add_column("Valor", justify = "right")
        saldo = procura_saldo(cliente, opcoes, saldos)
        for data, descricao, valor in saldo["extratos"]:
            if (not inicio or data >= inicio) and (not fim or data <= fim):
                tabela.add_row(data.strftime("%Y-%m-%d %H:%M:%S"), descricao, formatar_valor(valor))
        console.print(tabela)
    except:
        console.print("[bold red]Verifique se colocou a data corretamente![/bold red]")

def exibir_extrato_filtro_valores(cliente, opcoes, saldos):
    try:
        console.print("[bold cyan]Extrato filtrado por valores[/bold cyan]")
        preferencia = encontrar_preferencias(opcoes, cliente["documento"])
        if preferencia["exibir_saldo"] == True:
            console.print(f"0. Voltar\t1. Filtrar\t{consultar_saldo(cliente, opcoes, saldos)}")
        else:
            console.print(f"0. Voltar\t1. Filtrar")
        min = None
        max = None
        while not min and not max:
            if preferencia["moeda_padrao"] == "BRL":
                min = float(input(f"Valor Minimo: R$ "))
                max = float(input(f"Valor Maximo: R$ "))
            elif preferencia["moeda_padrao"] == "EUR":
                min = float(input(f"Valor Minimo: € "))
                max = float(input(f"Valor Maximo: € "))
            else:
                min = float(input(f"Valor Minimo: US$ "))
                max = float(input(f"Valor Maximo: US$ "))
        tabela = Table(title = "Extrato")
        tabela.add_column("Data", justify = "left")
        tabela.add_column("Descrição", justify = "left")
        tabela.add_column("Valor", justify = "right")
        saldo = procura_saldo(cliente, opcoes, saldos)
        for data, descricao, valor in saldo["extratos"]:
            if (valor >= min) and (valor <= max):
                tabela.add_row(data.strftime("%Y-%m-%d %H:%M:%S"), descricao, formatar_valor(valor, preferencia["moeda_padrao"]))
        console.print(tabela)
    except:
        console.print("[bold red]Ops! Algum imprevisto aconteceu![/bold red]")

def menu_extrato(cliente, opcoes, saldos):
    opcao = getpass.getpass("")
    while True:
        if opcao == "0" or not opcao:
            break
        elif opcao == "1":
            print("\n1. Filtrar por data")
            print("2. Filtrar por valores")
            print("0. Cancelar Filtragem")
            opcao_two = input("Escolha uma opcao: ")
            if opcao_two == "1":
                exibir_extrato_filtro_data(cliente, opcoes, saldos)
            elif opcao_two == "2":
                exibir_extrato_filtro_valores(cliente, opcoes, saldos)
            elif opcao_two == "0":
                break
            else:
                console.print("[bold red]Opcão invalida![/bold red]")
        else:
            console.print("[bold red]Opcão invalida![/bold red]")