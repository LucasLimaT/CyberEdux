numero = int(input("Digite um número: "))
potencia = 1
while potencia < numero:
    potencia = potencia * 10
while potencia >= 1:
    digito = numero // potencia
    numero = numero % potencia
    potencia = potencia / 10
    print(int(digito))
