def concluir_tarefas(concluidas, tarefas):
    tarefaConcluida = input("Qual tarefa foi concluida?:\n")
    if tarefas.remove(tarefaConcluida) == True:
        concluidas.append(tarefaConcluida)
    return concluidas