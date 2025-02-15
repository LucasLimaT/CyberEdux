def adicionar_tarefas(tarefas):
    tarefa_nova = input("Qual tarefa deseja adicionar?\n")
    if tarefas.count(tarefa_nova) != 0:
        tarefas.remove(tarefas.index(tarefa_nova))
    tarefas.insert(0, tarefa_nova)
    return tarefas