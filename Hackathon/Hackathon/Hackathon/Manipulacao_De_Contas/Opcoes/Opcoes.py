def criar_preferencias(conta):
    try:
        opcao = {
            "documento": conta["documento"],
            "moeda_padrao": "BRL",
            "nome_chamado": conta["nome"],
            "idioma": "PT",
            "exibir_saldo": True
        }
        return opcao
    except:
        print("Erro ao criar preferencias!")

def encontrar_preferencias(preferencias, documento):
    for preferencia in preferencias:
        if preferencia["documento"] == documento:
            return preferencia
    return None

def atualiza_preferencias(preferencia, preferencias): 
    for i in preferencias:
        if i["documento"] == preferencia["documento"]:
            pos = preferencias.index(i)
            preferencias[pos] = preferencia
            break
    return