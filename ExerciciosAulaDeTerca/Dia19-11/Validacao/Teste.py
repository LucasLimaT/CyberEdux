import Validar

while True:
    cpf = str(input("Digite um cpf:\nxxx.xxx.xxx-xx\n")).strip()
    if Validar.validar_CPF(cpf) == True:
        break

while True:
    email = input("Digite seu email: ").strip()
    if Validar.validar_Email(email) == True:
        break

while True:
    telefone = input("Forneca o seu telefone: \n(xx) xxxx-xxxx\n").strip()
    if Validar.validar_telefone(telefone) == True:
        break

while True:
    data = input("Forneca uma data: \ndd/mm/yyyy\n").strip()
    if Validar.validar_data(data) == True:
        break

senha = input("Forneca uma senha:\n").strip()
texto = Validar.validar_senha(senha)
while True:
    print(texto)
    if texto == "Senha Fraca":
        senha = input("Forneca uma senha mais forte:\n").strip()
        texto = Validar.validar_senha(senha)
    else:
        break



    