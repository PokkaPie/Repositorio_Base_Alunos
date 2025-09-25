alunos = 
    {"nome:":"Joao", "idade":20, "nota": 7.5}
    {"nome:":"Maria", "idade":18, "nota": 8.2}
    {"nome:":"Pedro", "idade":19, "nota": 6.8}
    {"nome:":"Ana", "idade":21, "nota": 9.0}
]

total_notas = 0
qunatidade_alunos = len(alunos)

for aluno in alunos:
    total_notas += aluno["nota"]
media_notas = total_notas/ qunatidade_alunos
print(f"A Média das notas dos alunos é {media_notas:.2f}")