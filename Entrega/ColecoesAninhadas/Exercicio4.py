alunos = [
    {"nome": "Carlos", "notas": [6.0, 7.0, 8.0]},
    {"nome": "Lucia", "notas": [9.0, 8.5, 10.0]},
    {"nome": "Pedro", "notas": [5.0, 4.5, 6.0]}
]

medias = list()

for aluno in alunos:
    medias.append((sum(aluno["notas"]))/3)

i = int(0)
for media in medias:
    if media > 7:
        print(alunos[i]["nome"])
    i += 1