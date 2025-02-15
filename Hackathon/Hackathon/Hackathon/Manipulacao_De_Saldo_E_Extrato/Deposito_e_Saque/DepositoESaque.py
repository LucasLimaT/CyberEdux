from datetime import datetime
from rich.console import Console
console = Console()

def depositar(saldo):
    try:
        console.print("[bold turquoise2]Depósito[/bold turquoise2]")
        valor = float(input(f"Valor do deposito: {verifica_moeda_padrao(saldo["moeda_padrao"])}"))
        if valor <= 0:
            console.print("[bold red]Valor inválido![/bold red]")
            return None
        saldo["saldo"] += valor
        saldo["extratos"].append((datetime.now(), "deposito", valor))
        console.print("[bold green]Depósito realizado com sucesso![/bold green]")
        return saldo
    except:
        console.print("[bold red]Ocorreu algum imprevisto ao realizar o deposito![/bold red]")

def sacar(saldo):
    try:
        console.print("[bold cyan]Saque[/bold cyan]")
        valor = float(input(f"Valor a sacar: {verifica_moeda_padrao(saldo["moeda_padrao"])}"))
        if valor <= 0 or valor > saldo["saldo"]:
            console.print("[bold red]Valor inválido! Verifique seu saldo![/bold red]")
            return None
        saldo["saldo"] -= valor
        saldo["extratos"].append((datetime.now(), "saque", -valor))
        console.print("[bold green]Saque realizado com sucesso![/bold green]")
        return saldo
    except:
        console.print("[bold red]Ocorreu algum imprevisto ao realizar o saque![/bold red]")

def verifica_moeda_padrao(moeda):
    if moeda == "BRL":
        return f"R$ "
    elif moeda == "EUR":
        return f"€ "
    else:
        return f"US$ "