# Criando uma função que calcula a media da turma e quem  foi aprovado ou reprovado
def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):

    # Criando variáveis com o valor total das notas
    total_notas = 0
    # Número de alunos (usa o método "len" que informa a quantidade de propriedades contidas no objeto notas)
    num_alunos = len(notas)
    # Criando arrays para os alunos aprovados e reprovados
    aprovados = []
    reprovados = []

    # Usando o loop For In para percorrer sobre as notas (e separando em variaveis "aluno" e "nota")
    for aluno, nota in notas.items():
        # Somando a nota na variavel das notas totais
        total_notas += nota
        # Caso a nota seja maior ou igual ao minimo para ser aprovado, entao o nome do aluno é adicionado ao array de aprovados
        if nota >= nota_minima_aprovacao:
            aprovados.append(aluno)
        # Se não será adicionado a lista de reprovados
        else:
            reprovados.append(aluno)

    # Calculando a media da turma
    media_turma = total_notas / num_alunos

    # Retornando os valores da media da turma e os arrays de aprovados e reprovados
    return media_turma, aprovados, reprovados

# Criando a variavel "notas" que tem o valor dos Alunos e suas respectivas Notas
notas = {
    "Alice": 85,
    "Bruno": 72,
    "Carlos": 60,
    "Diana": 95,
    "Eduardo": 55
}

# Criando a variavel que informa a nota minima para ser aprovado
nota_minima_aprovacao = 70

# Chamando a função
media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)

# Imprimindo os resultados
print(f"Média da turma: {media_turma:.2f}")
print(f"Alunos aprovados: {', '.join(aprovados)}")
print(f"Alunos reprovados: {', '.join(reprovados)}")