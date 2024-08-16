# Criando a função que calcula o custo de uma viagem de acordo com a distancia da viagem, custo de combustivel, consumo do veiculo, pedagios e seus respectivos custos
def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios,
custo_pedagio):

    # Atribuindo valoes as variaveis de custos (usando matematica e de acordo com os valores recebidos na chamada da função)
    custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel

    custo_pedagio_total = numero_pedagios * custo_pedagio

    custo_total = custo_combustivel_total + custo_pedagio_total

    # Retornando os valores calculados
    return custo_total, custo_combustivel_total, custo_pedagio_total

# Criando as variaveis que a função requisita e solicitando ao usuário para digitar seus valores
# Transofrmando todos os valores recebidos para numeros decimais com o metodo "float"
# Usando o metodo "int" no valor dos pedagios para transformar o valor em numero inteiro
distancia = float(input("Digite a distância da viagem (em km): "))
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): "))
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): "))
numero_pedagios = int(input("Digite o número de pedágios no percurso: "))
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): "))

# Chamando a função e recebendo os valores nas variaveis
custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios, custo_pedagio)

# Imprimindo os valores recebidos da função
print(f"Custo total da viagem: R${custo_total:.2f}")
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}")
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}")