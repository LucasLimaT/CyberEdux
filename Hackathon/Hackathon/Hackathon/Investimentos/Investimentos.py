from rich.console import Console
console = Console()

def simular_investimento():
    try:
        console.print("[bold cyan]Simulação de Investimento[/bold cyan]")
        valor = float(input("Valor que deseja investir: R$ "))
        if valor <= 0:
            console.print("[bold red]Valor inválido![/bold red]")
            return 
        console.print("[bold steel_blue]Opções de investimento:[/bold steel_blue]")
        opcao = input("1. CDB\n2. Tesouro Direto\nEscolha uma opção: ")
        if opcao == "1":
            console.print("CDB:")
            console.print(f"1. Curto Prazo (até 6 meses): 80% do CDI")
            console.print(f"2. Médio Prazo (6 meses a 2 anos): 115% do CDI")
            console.print(f"3. Longo Prazo (mais de 2 anos): 130% do CDI")
            selecione = input("Selecione uma opção: ")
            if selecione == "1":
                taxa_juros = 0.8
            elif selecione == "2":
                taxa_juros = 1.15
            elif selecione == "3":
                taxa_juros = 1.3
            else:
                console.print("[bold red]Opção inválida![/bold red]")
                return 
        elif opcao == "2":
            console.print("Tesouro Direto:")
            console.print(f"1. Curto Prazo (até 1 ano): 85% do CDI (taxa menor por conta da isenção de IR)")
            console.print(f"2. Médio Prazo (1 a 3 anos): 95% a 105% do CDI")
            console.print(f"3. Longo Prazo (mais de 3 anos): 110% do CDI")
            selecione = input("Selecione uma opção: ")
            if selecione == "1":
                taxa_juros = 0.85
            elif selecione == "2":
                taxa_juros = 0.95
            elif selecione == "3":
                taxa_juros = 1.05
            else:
                console.print("[bold red]Opção inválida![/bold red]")
                return 
        else:
            console.print("[bold red]Opção inválida![/bold red]")
            return 
        anos = int(input("Período em anos: "))
        montante = valor * (1 + taxa_juros) ** anos
        console.print(f"[bold green]Após {anos} anos, seu investimento de R$ {valor:.2f} será R$ {montante:.2f}[/bold green]")
    except ValueError:
        console.print("[bold red]Ops! Algum imprevisto aconteceu! Verifique os dados inseridos.[/bold red]")
        return 
    except Exception as e:
        console.print(f"[bold red]Erro inesperado: {e}[/bold red]")
        return 
    
def formatar_valor(valor, moeda):
    if moeda == "BRL":
        return f"R$ {valor:.2f}"
    elif moeda == "EUR":
        return f"€ {valor:.2f}"
    else:
        return f"US$ {valor:.2f}"