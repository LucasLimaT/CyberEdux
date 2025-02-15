def verTarefas(tarefas, concluidas):
    print("Tarefas que precisam ser realizadas:\n")
    for i in range(len(tarefas)):
        print(f"{i+1}ª {tarefas[i]}\n")
    print("Tarefas ja realizadas:\n")
    for i in range(len(concluidas)):
        print(f"{i+1}ª {concluidas[i]}\n")
