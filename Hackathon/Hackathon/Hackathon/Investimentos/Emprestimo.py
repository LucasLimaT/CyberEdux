from rich.console import Console
console = Console()

def simular_emprestimo():
    try:
        console.print("[bold cyan] Simulação de Emprestimo[/bold cyan]")
        valor = float(input("Emprestimo de 2000 a 10.000: R$ "))
        if 2000 > valor or valor > 10000:
            console.print("[bold red]Valor inválido![/bold red]")
            return
        taxa_juros = 0.05
        tempo = float(input("Quantos anos: "))
        console.print(f"Valor das parcelas será: {taxa_juros/(1-1/(taxa_juros+1))**tempo:.2f}")
    except:
        console.print("[bold red]Ocorreu algo inesperado![/bold red]")