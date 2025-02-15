def listar_cadastros(cadastros):
    print("\n\tAlunos:")
    alunos_ordenados = sorted(cadastros, key=lambda x: x["matricula"])
    if not alunos_ordenados:
        print("\tNenhum aluno cadastrado.")
        return
    print("_"*75)
    print("|\tMatricula\t|\tAluno\t|\tIdade\t|\tCurso\t|")
    print("="*75)
    for i, aluno in enumerate(alunos_ordenados, start=1):
        print(f"|\t{aluno["matricula"]}\t\t|\t{aluno["nome"]}\t|\t{aluno["idade"]}\t|\t{aluno["curso"]}\t|")
    print("="*75)

def cadastro(cadastros):
    try:
        print("\n\tCADASTRO")
        if not cadastros:
            matricula = 1
        else:
            matricula = int(len(cadastro) + 1)
        nome = str(input("Nome completo: ")).strip().lower()
        nome = nome.capitalize()
        idade = int(input("Idade: "))
        curso = input("Curso: ")
        conta = {
                "nome": nome,
                "idade": idade,
                "curso": curso,
                "matricula": matricula
                }
        return conta
    except:
        print("Erro ao fazer cadastro!")
        return

def encontrar_aluno(cadastros, dadosProcurados):
    try:
        for aluno in cadastros:
            if dadosProcurados.isdigit():
                if aluno["matricula"] == int(dadosProcurados):
                    return aluno
            elif aluno["nome"] == dadosProcurados:
                return aluno
        return None
    except Exception as e:
        print("Aluno não encontrado!", e)

def mudar_dados(cadastros):
    try:
        nome = input("Nome do aluno que deseja procurar: ")
        aluno = encontrar_aluno(cadastros, nome)
        if not aluno:
            print("aluno não encontrado!")
            return
        novo_curso = input(f"Novo curso do {nome}: ")
        aluno["curso"] = novo_curso
        nova_idade = input(f"Nova idade do {nome}: ")
        aluno["idade"] = nova_idade
        atualiza_dados(cadastros, aluno)
    except:
        print("Erro ao mudar pontuação")

def atualiza_dados(alunos, aluno): 
    for i in alunos:
        if i["nome"] == aluno["nome"]:
            pos = alunos.index(i)
            alunos[pos] = aluno
            break
    return

def excluir_aluno(alunoQueSeraExcluido, cadastros):
    aux = alunoQueSeraExcluido["nome"]
    alunoQueSeraExcluido["nome"] = None
    alunoQueSeraExcluido["matricula"] = None
    alunoQueSeraExcluido["idade"] = None
    alunoQueSeraExcluido["curso"] = None
    for i in cadastros:
        if i["nome"] == aux:
            pos = cadastros.index(i)
            cadastros[pos] = alunoQueSeraExcluido
            break
    return
    