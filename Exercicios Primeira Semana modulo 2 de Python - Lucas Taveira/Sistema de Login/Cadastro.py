import Validar

def cadastro(contas):
    print("\n\tCADASTRO")
    while True:
        usuario = str(input("Usuario: ")).strip()
        if not encontrar_usuario(contas, usuario):
            break
        print("\nUsuario já cadastrado!")
    nome = str(input("Nome completo: ")).strip().lower()
    nome = nome.capitalize()
    senha = input("Senha: ").strip()
    texto = Validar.validar_senha(senha)
    while True:
        print(texto)
        if texto == "Senha Fraca":
            senha = input("Forneca uma senha mais forte:\n").strip()
            texto = Validar.validar_senha(senha)
        else:
            break
    conta = {
            "usuario": usuario,
            "nome": nome,
            "senha": senha
            }
    return conta

def encontrar_usuario(contas, usuario):
    try:
        for cliente in contas:
            if cliente["usuario"] == usuario:
                return cliente
        return None
    except Exception as e:
        print(" Não existe cliente", e)