soma = float(0)
aluno = {"Lucas": 10, "Marcelo": 9, "Pedro": 8}
soma += aluno.get("Lucas")
soma += aluno.get("Marcelo")
soma += aluno.get("Pedro")
soma = soma/3
print(f"{soma:.2f}")