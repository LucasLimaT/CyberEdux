from API_Principal.Login import login
from API_Principal.Menu import menu
from Integracao_Com_Dispositivo.Manipulacao_De_Arquivos.Arquivos import pegar_dados, pegar_saldos, salvar_dados, salvar_saldos
from rich.console import Console
console = Console()

contas = []
preferencias = []
saldos = []

try:
    print(f"███╗   ██╗██████╗ ██╗  ██╗\n████╗  ██║██╔══██╗██║ ██╔╝\n██╔██╗ ██║██████╔╝█████╔╝\n██║╚██╗██║██╔══██╗██╔═██╗\n██║ ╚████║██████╔╝██║  ██╗\n╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝\n{"NOOB BANK".center(27)}")
    contas = pegar_dados("Contas.txt")
    preferencias = pegar_dados("Opcoes.txt")
    saldos = pegar_saldos()
    usuario_logado = login(contas, preferencias, saldos)
    menu(usuario_logado, contas, saldos, preferencias)
    salvar_dados("Opcoes.txt", preferencias)
    salvar_dados("Contas.txt", contas)
    salvar_saldos(saldos)
except:
    console.print("[bold red]Podia dar problema em todos os lugares possiveis, menos aqui!\nSe deu ruim aqui f*![/bold red]")