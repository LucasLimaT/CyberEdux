texto = input("Digite um texto: ").strip()
texto = texto.lower()
texto = texto.replace(".", "")
texto = texto.replace(",", "")
texto = texto.replace("!", "")
texto = texto.replace("?", "")
texto = texto
texto = texto.split()
adicionou = False
dicionario = {}
palavra_de_maior_valor = None
palavra_de_segundo_maior_valor = None
palavra_de_terceiro_maior_valor = None
maior_valor = int(0)
segundo_maior_valor = int(0)
terceiro_maior_valor = int(0)
for palavras in texto:
    dicionario[palavras] = texto.count(palavras)
print(dicionario)
new_list = []
for key, values in dicionario.items():
    if values > maior_valor:
        terceiro_maior_valor = segundo_maior_valor
        palavra_de_terceiro_maior_valor = palavra_de_segundo_maior_valor
        segundo_maior_valor = maior_valor
        palavra_de_segundo_maior_valor = palavra_de_maior_valor
        maior_valor = values
        palavra_de_maior_valor = key
    elif values > segundo_maior_valor:
        terceiro_maior_valor = segundo_maior_valor
        palavra_de_terceiro_maior_valor = palavra_de_segundo_maior_valor
        segundo_maior_valor = values
        palavra_de_segundo_maior_valor = key
    elif values > terceiro_maior_valor:
        terceiro_maior_valor = values
        palavra_de_terceiro_maior_valor = key
print(f"Palavra de maior frequencia: {palavra_de_maior_valor}\nQuantidade de vezes que a palavra de maior valor aparece: {maior_valor}")
print(f"\nPalavra de segundo maior frequencia: {palavra_de_segundo_maior_valor}\nQuantidade de vezes que a palavra de segundo maior valor aparece: {segundo_maior_valor}")
print(f"\nPalavra de terceiro maior frequencia: {palavra_de_terceiro_maior_valor}\nQuantidade de vezes que a palavra de terceiro maior valor aparece: {terceiro_maior_valor}")
print("Palavras que aparecem apenas 1 vez: ")
for key, values in dicionario.items():
    if values == 1:
        print(key)
