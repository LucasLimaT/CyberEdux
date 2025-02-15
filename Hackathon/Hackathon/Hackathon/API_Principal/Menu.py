from Funcionalidades_Diversas.Limpar_Console import limpar_console
from Funcionalidades_Diversas.Configuracoes import atualizar_dados, consultar_dados, excluir_conta, mudar_moeda_padrao, mudar_nome_preferencia
from Investimentos.Emprestimo import simular_emprestimo
from Mudanca_De_Cambio.Cambio import comprar_cambio
from Investimentos.Investimentos import simular_investimento
from Manipulacao_De_Contas.Opcoes.Opcoes import atualiza_preferencias, encontrar_preferencias
from Manipulacao_De_Saldo_E_Extrato.Extrato import exibir_extrato
from Tranferencias_Bancarias.Transferencias import menu_transferencias
from Manipulacao_De_Saldo_E_Extrato.Manipulacao_De_Saldo import consultar_saldo, menu_saldo_deposito_saque
from rich.console import Console
console = Console()

def menu(usuario_logado, contas, saldos, preferencias):
    try:
        while True:
            if usuario_logado["documento"] != "Conta_Exlcuida":
                preferencia = encontrar_preferencias(preferencias, usuario_logado["documento"])
                print(f"███╗   ██╗██████╗ ██╗  ██╗\n████╗  ██║██╔══██╗██║ ██╔╝\n██╔██╗ ██║██████╔╝█████╔╝\n██║╚██╗██║██╔══██╗██╔═██╗\n██║ ╚████║██████╔╝██║  ██╗\n╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝\n{"NOOB BANK".center(27)}")
                console.print("\n[bold yellow]Menu Principal[/bold yellow]")
                if preferencia["exibir_saldo"] == True:
                    console.print(f"[bold green]Olá, {preferencia["nome_chamado"]}![/bold green]\t{consultar_saldo(usuario_logado, preferencias, saldos)}")
                else: 
                    console.print(f"[bold green]Olá, {preferencia["nome_chamado"]}![/bold green]")
                console.print("1. Saque e Depósito")
                console.print("2. Transferencia")
                console.print("3. Investimentos")
                console.print("4. Extrato")
                console.print("5. Compra De Cambio")
                console.print("6. Simular emprestimo")
                console.print("7. Configurações")
                console.print("0. Sair")

                opcao = input("Escolha uma opção: ")

                if opcao == "1":
                    limpar_console()
                    menu_saldo_deposito_saque(usuario_logado, preferencias, saldos)
                elif opcao == "2":
                    limpar_console()
                    menu_transferencias(usuario_logado, contas, preferencias, saldos)
                elif opcao == "3":
                    limpar_console()
                    simular_investimento()
                elif opcao == "4":
                    limpar_console()
                    exibir_extrato(usuario_logado, preferencias, saldos)
                elif opcao == "5":
                    limpar_console()
                    comprar_cambio(usuario_logado, preferencias, saldos)
                elif opcao == "6":
                    limpar_console()
                    simular_emprestimo()
                elif opcao == "7":
                    limpar_console()
                    configuracoes(usuario_logado, contas, preferencias)
                elif opcao == "0":
                    console.print("[bold cyan]Obrigado por usar o Noob Bank![/bold cyan]")
                    break
                else:
                    console.print("[bold red]Opção inválida![/bold red]")
            else:
                break
    except:
        console.print("[bold red]Ops! Algum imprevisto aconteceu![/bold red]")

def configuracoes(usuario_logado, contas, preferencias):
    while True:
        preferencia = encontrar_preferencias(preferencias, usuario_logado["documento"])
        console.print("⚙️\t[bold blue]Configurações[/bold blue]")
        console.print("1. Mudar Moeda Padrão")
        console.print("2. Mudar nome pelo qual quer ser chamado")
        console.print("3. Atualizar dados da conta")
        if preferencia["exibir_saldo"] == True:
            console.print("4. Esconder saldo")
        else:
            console.print("4. Mostrar saldo")
        console.print("5. Consultar Dados Bancarios")
        console.print("6. Excluir conta")
        console.print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mudar_moeda_padrao(preferencia, preferencias)
        elif opcao == "2":
            mudar_nome_preferencia(preferencia, preferencias)
        elif opcao == "3":
            atualizar_dados(usuario_logado, contas)
        elif opcao == "4":
            preferencia["exibir_saldo"] = not preferencia["exibir_saldo"]
            atualiza_preferencias(preferencia, preferencias)
        elif opcao == "5":
            consultar_dados(usuario_logado)
        elif opcao == "6":
            excluir_conta(usuario_logado, contas)
            break
        elif opcao == "0":
            break
        else:
            console.print("[bold red]Opção inválida![/bold red]")
            