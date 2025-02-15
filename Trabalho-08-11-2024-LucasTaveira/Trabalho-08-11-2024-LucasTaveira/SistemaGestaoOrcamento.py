menu = int(1)
continuar = bool(True)
saldo = float(0)
numeroDeReceitas = int(0)
numeroDeDespesas = int(0)
tipoDespesa = [int(-1)]
receitas = []
despesas = []
alimentacao = float(0)
transporte = float(0)
lazer = float(0)
outros = float(0)
continuarInserindoReceita = bool(True)
continuarInserindoDespesas = bool(True)
while(continuar == True):
    menu = int(input("\nEscolha uma das seguintes opcoes:\n[1] Inserir Receitas\n[2] Inserir Despesas\n[3] Extrato\n[4] Relatorio\n[5] Sair\n\n"))
    continuarInserindoReceita = True
    continuarInserindoDespesas = True
    if menu == 1:
        while continuarInserindoReceita == True:
            receitas.append(float(input(f"Digite a receita Nº {numeroDeReceitas+1}: ")))
            saldo += receitas[numeroDeReceitas]
            print("Saldo atual: R$", saldo, "\n")
            numeroDeReceitas += 1
            continuarInserindo = input("Deseja continuar inserindo receitas?\n[Y] Sim\t[N] Não\n").upper()
            if continuarInserindo != 'Y':
                continuarInserindoReceita = False
    elif menu == 2:
        while continuarInserindoDespesas == True:
            while 0 >= tipoDespesa[numeroDeDespesas] or tipoDespesa[numeroDeDespesas] >= 5:
                tipoDespesa[numeroDeDespesas] = int(input("Informe o tipo da despesa:\n[1] Alimentacao\n[2] Transporte\n[3] Lazer\n[4] Outros\n\n"))
            despesas.append(float(input(f"Digite a despesa Nº {numeroDeDespesas+1}: ")))
            saldo -= despesas[numeroDeDespesas]
            print("Saldo atual: R$", saldo, "\n")
            if tipoDespesa[numeroDeDespesas] == 1:
                alimentacao += despesas[numeroDeDespesas]
            elif tipoDespesa[numeroDeDespesas] == 2:
                transporte += despesas[numeroDeDespesas]
            elif tipoDespesa[numeroDeDespesas] == 3:
                lazer += despesas[numeroDeDespesas]
            else:
                outros += despesas[numeroDeDespesas]
            tipoDespesa.append(-1)
            numeroDeDespesas += 1
            continuarInserindo = input("Deseja continuar inserindo despesas?\n[Y] Sim\t[N] Não\n").upper()
            if continuarInserindo != 'Y':
                continuarInserindoDespesas = False
    elif menu == 3:
        tam = len(receitas)
        print(" ---------------------------------------\n",
                "Receitas:\n",
                "---------------------------------------\n",)
        for i in range(tam):
            print(" Receita Nº", i+1, ": R$", receitas[i])
        tam = len(despesas)
        print(" ---------------------------------------\n",
                "Despesas:\n",
                "---------------------------------------\n",)
        for i in range(tam):
            if tipoDespesa[i] == 1:
                print(" Despesa Nº", i+1, ": R$", despesas[i], "\tTipo: Alimentacao")
            elif tipoDespesa[i] == 2:
                print(" Despesa Nº", i+1, ": R$", despesas[i], "\tTipo: Transporte")
            elif tipoDespesa[i] == 3:
                print(" Despesa Nº", i+1, ": R$", despesas[i], "\tTipo: Lazer")
            else:
                print(" Despesa Nº", i+1, ": R$", despesas[i], "\tTipo: Outros")
        print(" ---------------------------------------\n",
                "Saldo atual: R$", saldo, "\n",
                "---------------------------------------\n",)
    elif menu == 4:
        soma = float(0)
        total = outros + lazer + transporte + alimentacao
        print("-----------------------------------------------------")
        for i in range(len(receitas)):
            soma += receitas[i]
        print("Total das receitas:", soma)
        print("-----------------------------------------------------")
        if alimentacao > transporte >= lazer >= outros:
            print("Area que teve a maior despesa: Alimentacao")
            print("Total dos gastos nesta area:", alimentacao)
        elif transporte > lazer >= outros:
            print("Area que teve a maior despesa: Transporte")
            print("Total dos gastos nesta area:", transporte)
        elif lazer > outros:
            print("Area que teve a maior despesa: lazer")
            print("Total dos gastos nesta area:", lazer)
        elif outros > alimentacao:
            print("Area que teve a maior despesa: Outros")
            print("Total dos gastos nesta area:", outros)
        else:
            print("Area que teve a maior despesa: Gastos Indeterminados")
            print("Total dos gastos:", total)
        print("-----------------------------------------------------")
        print("Total das despesas:", total)
        print("-----------------------------------------------------")
    elif menu == 5:
        continuar = False
    else:
        print("\nOpcao Invalida!")