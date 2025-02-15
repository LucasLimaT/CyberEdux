import ast
from datetime import datetime

def ler_arquivo(nome):
    try:
        file = open(nome, "r", encoding='utf-8')
        mensagem = file.read()
        file.close()
        return mensagem
    except:
        return None

def escrever_no_arquivo(nome, conteudo):
    try:
        novo_conteudo = ler_arquivo(nome) + "\n" + conteudo
        file = open(nome, "w", encoding='utf-8')
        file.write(novo_conteudo)
        file.close()
    except:
        print("\nErro ao escrever no arquivo!")

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
        return dados
    except FileNotFoundError:
        print(f"O arquivo {nome} não foi encontrado.")
        return []
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return []

def verifica_se_ja_existe(nome):
    try:
        file = open(nome, "x")
        file.close()
        return False
    except:
        print("\nJá existe um arquivo com esse nome!")
        return True
    
def salvar_saldos(saldos):
    try:
        with open("Saldos.txt", "w", encoding='utf-8') as arquivo:
            for item in saldos:
                item["extratos"] = [
                    (extrato[0], extrato[1] if len(extrato) > 1 and extrato[1] else "Descrição não informada", extrato[2])
                    if len(extrato) == 3 else
                    (extrato[0], "Descrição não informada", extrato[1])
                    for extrato in item["extratos"]
                ]
                arquivo.write(f"Usuario: {item['usuario']}\n")
                arquivo.write(f"Moeda: {item['moeda_padrao']}\n")
                arquivo.write(f"Saldo: {item['saldo']}\n")
                arquivo.write("Extratos:\n")
                for extrato in item["extratos"]:
                    arquivo.write(f"  - {extrato}\n")
                arquivo.write("\n" + "="*40 + "\n")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def pegar_saldos():
    try:
        saldos = []
        with open("Saldos.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip().split("=" * 40)
            for registro in conteudo:
                linhas = registro.strip().splitlines()
                usuario = None
                moeda = None
                saldo = None
                extratos = []
                for linha in linhas:
                    if linha.startswith("Usuario:"):
                        usuario = linha.split(":")[1].strip()
                    elif linha.startswith("Moeda:"):
                        moeda = linha.split(":")[1].strip()
                    elif linha.startswith("Saldo:"):
                        saldo = float(linha.split(":")[1].strip())
                    elif linha.startswith("-"):
                        try:
                            partes = linha.split(" - ")
                            if len(partes) == 3:
                                data = datetime.strptime(partes[0].strip(), "%Y-%m-%d %H:%M:%S.%f")
                                descricao = partes[1].strip() if partes[1].strip() else "Descrição não informada"
                                valor = float(partes[2].strip())
                                extratos.append((data, descricao, valor))
                            else:
                                print(f"Formato de extrato inválido (deve ter 3 partes): {linha}")
                        except Exception as e:
                            print(f"Erro ao processar extrato: {linha} -> {e}")
                saldos.append({
                    "usuario": usuario,
                    "moeda_padrao": moeda,
                    "saldo": saldo,
                    "extratos": extratos
                })
        return saldos
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return []