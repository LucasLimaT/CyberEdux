import getpass
from Manipulacao_De_Contas.Opcoes.Opcoes import encontrar_preferencias
from Manipulacao_De_Contas.Cadastro.Cadastro import cadastro
from rich.console import Console
console = Console()

def login(contas, preferencias, saldos):
    while True:
        opcao = getpass.getpass(f"\n[1] Login\n[2] Cadastro\n")
        if opcao == "1":
            console.print("[bold cyan]Login[/bold cyan]")
            usuario = input("CPF ou CNPJ: ").strip()
            senha = getpass.getpass("Senha: ").strip()
            for conta in contas:
                if conta["documento"] == usuario and conta["senha"] == senha:
                    preferencia = encontrar_preferencias(preferencias, conta["documento"])
                    console.print(f"[bold green]Bem-vindo(a), {preferencia["nome_chamado"]}![/bold green]")
                    return conta
            console.print("[bold red]\nUsuario ou senha incorretos![/bold red]")
        elif opcao == "2":
            cadastro(contas, preferencias, saldos)