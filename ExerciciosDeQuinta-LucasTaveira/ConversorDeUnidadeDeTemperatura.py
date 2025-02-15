def converter_temperatura(graus):
    return (graus * 5/9) + 32

while True:
    print(f"A temperatura em fahrenheit é: {converter_temperatura(float(input("Digite a temperatura em graus que deseja converter: "))):.2f}")
    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break