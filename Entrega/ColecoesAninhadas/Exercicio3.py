contatos = {
 "João": {"telefone": "1234", "email": "joao@example.com"},
 "Ana": {"telefone": "5678", "email": "ana@example.com"}
}

print(contatos["Ana"])

contatos["Ana"]["telefone"] = "9999"

print(contatos["Ana"])