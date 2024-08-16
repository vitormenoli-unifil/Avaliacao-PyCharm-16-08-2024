# Criando a função que retorna para o usuário se ela está com Diabetes, Pré Diabético ou está normal
def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial):

    # Se o valor da glicemia em jejum for maior ou igual a 126 então o usuário está Diabético
    # Ou se a glicemia pós prandial for maior ou igual a 200 então o usuário também está Diabético
    # Caso nenhuma das condições seja verdadeira, será passada para o próximo if
    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200:
        # Faz a função retornar a string "Diabetes"
        return "Diabetes"
    # Caso a glicemia em jejum for maior ou igual a 100 então o usuário está Pre Diabetico
    # Ou se a glicemia pos prandial for maior ou igual a 140 então o usuário também está Pre Diabético
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:
        # Faz a função retornar a string "Pré-diabetes"
        return "Pré-diabetes"
    else:
    # Caso nenhuma condição seja verdadeira, então o usuário está Normal
        return "Normal"

# Recebendo os valores de glicemia e transformando eles em decimais com o método "float"
glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))

# Chamando a função e recebendo uma resposta
resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)
# Imprimindo a resposta da função
print(f"O diagnóstico é: {resultado}")