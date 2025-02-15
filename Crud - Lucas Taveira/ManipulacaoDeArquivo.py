import ast

def salvar_dados(nome, conteudo):
    try:
        file = open(nome, "w", encoding='utf-8')
        for item in conteudo:
            file.write(f"{str(item)}\n")
        file.close()
    except:
        print("\nErro ao salvar dados no arquivo!")

def pegar_dados(nome):
    dados = []
    try:
        with open(nome, "r", encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                try:
                    dado = ast.literal_eval(linha)
                    if isinstance(dado, dict):
                        dados.append(dado)
                    else:
                        print(f"A linha não é um dicionário válido: {linha}")
                except (ValueError, SyntaxError) as e:
                    print(f"Erro ao processar a linha: {linha}, erro: {e}")
        print("Arquivo atualizado com sucesso!")
        return dados
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return []