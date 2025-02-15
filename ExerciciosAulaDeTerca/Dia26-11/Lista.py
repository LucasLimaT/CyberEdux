from AdicionarTarefas import adicionar_tarefas
from ConcluirTarefas import concluir_tarefas
from VerTarefas import verTarefas

concluidas = list()
tarefas = list()
while True:
    opcao = input("\nO que deseja fazer?\n[1] Adicionar Tarefas\n[2] Marcar como concluida\n[3] Listar Tarefas\n[4] Alterar prioridade\n[5] Fechar programa\n")
    if opcao == '1' or opcao == '4':
        tarefas = adicionar_tarefas(tarefas)
        verTarefas(tarefas, concluidas)
    elif opcao == '2':
        concluidas = concluir_tarefas(concluidas, tarefas)
        verTarefas(tarefas, concluidas)
    elif opcao == '3':
        verTarefas(tarefas, concluidas)
    else:
        break
