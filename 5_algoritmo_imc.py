# Criando a função que calcula o IMC da pessoa, a partir do peso e altura informado
def calcular_imc(peso, altura):

    # Calculando o imc e retornado o valor
    imc = peso / (altura ** 2)
    return imc

# Criando a função que classifica o imc da pessoa
def classificar_imc(imc):

    # Utilizando o if e else para de acordo com o número do IMC calculado, retornar uma string com sua classificação
    # Usando em todos os ifs (caso o imc seja maior que, retorna valor X, se nao se for maior ou igual a retorna valor Y, e assim por diante)
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        # Caso não seja verdadeira nenhuma condição a cima, retorna "Obesidade grau 3"
        return "Obesidade grau 3"

# Criando a função que sugere algo para a pessoa, de acordo com sua classificação do imc
def sugestao_atividade_fisica(classificacao_imc):

    # Utilizando os sistem de If Else para se o valor de "classificacao_imc" (que é informado na chamada da função) for uma String X então a função retorna uma string XX, se "classificacao_imc" for Y então a função retorna YY, e assim por diante
    if classificacao_imc == "Abaixo do peso":
        return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em proteínas e calorias."
    elif classificacao_imc == "Peso normal":
        return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e natação, junto a um treino de força moderado."
    elif classificacao_imc == "Sobrepeso":
        return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além de exercícios de resistência."
    elif classificacao_imc == "Obesidade grau 1":
        return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um programa de reeducação alimentar."
    elif classificacao_imc == "Obesidade grau 2":
        return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e acompanhamento nutricional."
    else:
        # Caso nenhuma condição a cima seja verdadeira, retorna a string abaixo
        return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica, fisioterapia, e consultas regulares com um nutricionista."

# Criando as variaveis de peso e altura e transformando elas em numeros decimais
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# Chamando as tres funções e criando variaveis para o retorno delas
imc = calcular_imc(peso, altura)
classificacao_imc = classificar_imc(imc)
sugestao = sugestao_atividade_fisica(classificacao_imc)

# Imrpimindo os valores recebidos das funções
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao_imc}")
print(f"Sugestão de atividade física: {sugestao}")