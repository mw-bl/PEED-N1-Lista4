def encontrar_aluno_maior_nota(lista_alunos):
    maior_nota = float("-inf")
    nome_aluno_maior_nota = ""

    for aluno in lista_alunos:
        nota = aluno["nota"]
        if nota > maior_nota:
            maior_nota = nota
            nome_aluno_maior_nota = aluno["nome"]

    return nome_aluno_maior_nota

# Exemplo
alunos = [
    {"nome": "João", "nota": 8.5},
    {"nome": "Maria", "nota": 7.9},
    {"nome": "Pedro", "nota": 9.2},
    {"nome": "Ana", "nota": 8.7}
]

resultado = encontrar_aluno_maior_nota(alunos)

print("Aluno com maior nota:", resultado)
