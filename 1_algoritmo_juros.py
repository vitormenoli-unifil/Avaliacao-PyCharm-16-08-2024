# Criando uma função que calcula juros com atraso
valor_principal = 1000.00

def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso):
    # Criando as variáveis de taxa de juros diária e juros totais (usando apenas matemática) e atribuindo um valor a ela de acordo com os valores passados na chamada da função
    taxa_juros_diaria = taxa_juros_anual / 365 / 100
    juros = valor_principal * taxa_juros_diaria * dias_atraso

    # Criando a variável que recebe o valor total com os juros
    valor_total = valor_principal + juros
    # A função retorna esses dois valores (valor total e juros)
    return valor_total, juros

# Criando as variáveis com valores para a chamada da função
taxa_juros_anual = 5.0
dias_atraso = 30

# Chamando a função e recebendo os resultados
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)

# Impressão dos resultados
print(f"Valor total a ser pago: R${valor_total:.2f}")
print(f"Valor dos juros: R${juros:.2f}")