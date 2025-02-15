def validar_senha(senha):
    if len(senha) > 8:
        if senha.find("@") != None:
            return "Senha Forte"
        return "Senha Razoavel"
    else:
        return f'Senha Fraca, precisa conter pelo "@"!'