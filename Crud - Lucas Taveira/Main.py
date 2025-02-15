from ManipulacaoDeArquivo import pegar_dados, salvar_dados
from ManipulacaoDeConta import cadastro, encontrar_aluno, excluir_aluno, listar_cadastros, mudar_dados
cadastros = pegar_dados("Alunos.txt")

def menu(cadastros):
    try:
        while True:
            print("\n\tMenu")
            print("1. Cadastrar aluno")
            print("2. Listar todos os alunos cadastrados")
            print("3. Buscar por nome ou matricula")
            print("4. Editar dados de um aluno")
            print("5. Remover um aluno")
            print("6. Gravar dados em um arquivo")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                conta = cadastro(cadastros)
                cadastros.append(conta)
            elif opcao == "2":
                listar_cadastros(cadastros)
            elif opcao == "3":
                dadosProcurados = input("Digite a matricula ou o nome do aluno que deseja procurar: ")
                aluno = encontrar_aluno(cadastros, dadosProcurados)
                if aluno is not None:
                    print("_"*72)
                    print("|\tMatricula\t|\tAluno\t|\tIdade\t|\tCurso\t|")
                    print("="*72)
                    print(f"|\t{aluno["matricula"]}\t|\t{aluno["nome"]}\t|\t{aluno["idade"]}\t|\t{aluno["curso"]}\t|")
                    print("="*72)
                else:
                    print("Aluno não encontrado!")
            elif opcao == "4":
                mudar_dados(cadastros)
            elif opcao == "5":
                alunoQueDesejaExcluir = input("Nome do aluno que deseja excluir: ")
                alunoQueDesejaExcluir = encontrar_aluno(cadastros, dadosProcurados)
                excluir_aluno(alunoQueDesejaExcluir, cadastros)
            elif opcao == "6":
                salvar_dados("Alunos.txt", cadastros)
            elif opcao == "0":
                print("Saindo...")
                return "N"
            else:
                print("Opção inválida!")
    except:
        print("Ops! Algum imprevisto aconteceu!")

while True:
    continuar = menu(cadastros)
    if continuar == "N":
        salvar_dados("Alunos.txt", cadastros)
        break
